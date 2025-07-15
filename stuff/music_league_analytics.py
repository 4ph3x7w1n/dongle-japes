#!/usr/bin/env python3
"""
The Dongle Japes Music League Analytics
Comprehensive analysis of the Music League data to uncover insights, patterns, and entertaining metrics
"""

import csv
import json
from collections import defaultdict, Counter
from datetime import datetime
import statistics
import math

# Load all CSV files
def load_csv(filename):
    data = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

# Load data
competitors = load_csv('/mnt/e/Projects/dongle/stuff/competitors.csv')
rounds = load_csv('/mnt/e/Projects/dongle/stuff/rounds.csv')
submissions = load_csv('/mnt/e/Projects/dongle/stuff/submissions.csv')
votes = load_csv('/mnt/e/Projects/dongle/stuff/votes.csv')

# Core Dongle Japes members
CORE_MEMBERS = {
    '201cc8e3af8249c5ba57f2e8d6235fb2': 'Chris Manning',
    '529211ec9c42438f9162e38917f2eeef': 'Max Voorhees', 
    'aac8b2b830694c88ba1567e463def3ac': 'UnclePhil (adamhudzik55)',
    'd45b3a6a10ba40218745e3fe18f0d4b8': 'Dylan Graves'
}

# Create ID to name mapping
id_to_name = {comp['ID']: comp['Name'] for comp in competitors}
name_to_id = {comp['Name']: comp['ID'] for comp in competitors}

print("🎵 THE DONGLE JAPES MUSIC LEAGUE ANALYTICS 🎵")
print("=" * 60)

# Basic Stats
print(f"\n📊 BASIC STATS")
print(f"Total Competitors: {len(competitors)}")
print(f"Total Rounds: {len(rounds)}")
print(f"Total Submissions: {len(submissions)}")
print(f"Total Votes Cast: {len(votes)}")

# Round Analysis
print(f"\n🎯 ROUND ANALYSIS")
for round_data in rounds:
    round_name = round_data['Name']
    round_id = round_data['ID']
    round_submissions = [s for s in submissions if s['Round ID'] == round_id]
    round_votes = [v for v in votes if v['Round ID'] == round_id]
    
    print(f"\n🎪 {round_name}")
    print(f"   Description: {round_data['Description']}")
    print(f"   Submissions: {len(round_submissions)}")
    print(f"   Total Votes: {len(round_votes)}")
    if round_votes:
        avg_points = statistics.mean([int(v['Points Assigned']) for v in round_votes])
        print(f"   Average Points per Vote: {avg_points:.2f}")

# Submission Analysis by Member
submission_stats = defaultdict(lambda: {'count': 0, 'tracks': []})
for sub in submissions:
    submitter_id = sub['Submitter ID']
    submitter_name = id_to_name.get(submitter_id, submitter_id)
    submission_stats[submitter_name]['count'] += 1
    submission_stats[submitter_name]['tracks'].append({
        'title': sub['Title'],
        'artist': sub['Artist(s)'],
        'round': sub['Round ID'],
        'comment': sub.get('Comment', '')
    })

print(f"\n🎤 SUBMISSION STATS")
for name, stats in sorted(submission_stats.items(), key=lambda x: x[1]['count'], reverse=True):
    print(f"{name}: {stats['count']} submissions")

# Vote Analysis - Points Received
points_received = defaultdict(lambda: {'total': 0, 'count': 0, 'votes': []})
points_given = defaultdict(lambda: {'total': 0, 'count': 0, 'votes': []})

# Create mapping of track to submitter
track_to_submitter = {}
for sub in submissions:
    track_to_submitter[sub['Spotify URI']] = sub['Submitter ID']

for vote in votes:
    track_uri = vote['Spotify URI']
    voter_id = vote['Voter ID'] 
    points = int(vote['Points Assigned'])
    
    # Points received analysis
    if track_uri in track_to_submitter:
        submitter_id = track_to_submitter[track_uri]
        submitter_name = id_to_name.get(submitter_id, submitter_id)
        points_received[submitter_name]['total'] += points
        points_received[submitter_name]['count'] += 1
        points_received[submitter_name]['votes'].append(points)
    
    # Points given analysis  
    voter_name = id_to_name.get(voter_id, voter_id)
    points_given[voter_name]['total'] += points
    points_given[voter_name]['count'] += 1
    points_given[voter_name]['votes'].append(points)

print(f"\n🏆 POINTS RECEIVED LEADERBOARD")
for name, stats in sorted(points_received.items(), key=lambda x: x[1]['total'], reverse=True):
    if stats['count'] > 0:
        avg = stats['total'] / stats['count']
        print(f"{name}: {stats['total']} total points, {avg:.2f} avg per submission")

print(f"\n🎁 VOTING GENEROSITY (Points Given)")
for name, stats in sorted(points_given.items(), key=lambda x: x[1]['total'], reverse=True):
    if stats['count'] > 0:
        avg = stats['total'] / stats['count']
        print(f"{name}: {stats['total']} total given, {avg:.2f} avg per vote")

# Core Member Deep Dive
print(f"\n🌟 CORE DONGLE JAPES MEMBER ANALYSIS")
for member_id, member_name in CORE_MEMBERS.items():
    print(f"\n🎸 {member_name.upper()}")
    
    # Submissions
    member_subs = [s for s in submissions if s['Submitter ID'] == member_id]
    print(f"   Submissions: {len(member_subs)}")
    
    if member_subs:
        print(f"   Favorite Artists: {', '.join([s['Artist(s)'] for s in member_subs[:3]])}")
    
    # Points received
    if member_name in points_received:
        stats = points_received[member_name]
        if stats['count'] > 0:
            avg_received = stats['total'] / stats['count']
            print(f"   Average Points Received: {avg_received:.2f}")
            print(f"   Total Points Received: {stats['total']}")
            
            # Vote distribution
            vote_dist = Counter(stats['votes'])
            print(f"   Vote Distribution: {dict(vote_dist)}")
    
    # Points given
    if member_name in points_given:
        stats = points_given[member_name]
        if stats['count'] > 0:
            avg_given = stats['total'] / stats['count']
            print(f"   Average Points Given: {avg_given:.2f}")
            print(f"   Total Votes Cast: {stats['count']}")

# Controversial Songs Analysis (highest vote variance)
track_votes = defaultdict(list)
track_info = {}

for vote in votes:
    track_uri = vote['Spotify URI']
    points = int(vote['Points Assigned'])
    track_votes[track_uri].append(points)

for sub in submissions:
    track_info[sub['Spotify URI']] = {
        'title': sub['Title'],
        'artist': sub['Artist(s)'],
        'submitter': id_to_name.get(sub['Submitter ID'], sub['Submitter ID'])
    }

print(f"\n🔥 MOST CONTROVERSIAL SONGS (Highest Vote Variance)")
controversial = []
for track_uri, votes_list in track_votes.items():
    if len(votes_list) >= 3:  # Need at least 3 votes
        variance = statistics.variance(votes_list)
        if track_uri in track_info:
            controversial.append((variance, track_info[track_uri], votes_list))

for variance, info, votes_list in sorted(controversial, key=lambda x: x[0], reverse=True)[:5]:
    print(f"🎵 {info['title']} by {info['artist']}")
    print(f"   Submitted by: {info['submitter']}")
    print(f"   Votes: {votes_list} (variance: {variance:.2f})")

# Head-to-Head Analysis for Core Members
print(f"\n⚔️ HEAD-TO-HEAD: CORE MEMBERS VOTING ON EACH OTHER")
for voter_id, voter_name in CORE_MEMBERS.items():
    print(f"\n{voter_name} voting on other core members:")
    voter_votes = [v for v in votes if v['Voter ID'] == voter_id]
    
    for vote in voter_votes:
        track_uri = vote['Spotify URI']
        if track_uri in track_to_submitter:
            submitter_id = track_to_submitter[track_uri]
            if submitter_id in CORE_MEMBERS and submitter_id != voter_id:
                submitter_name = CORE_MEMBERS[submitter_id]
                points = vote['Points Assigned']
                track = next((s for s in submissions if s['Spotify URI'] == track_uri), None)
                if track:
                    print(f"   → {points} pts to {submitter_name} for '{track['Title']}'")

# Most Generous/Critical Voters
print(f"\n😇 MOST GENEROUS VOTERS (Highest Average Points Given)")
generous_voters = [(name, stats['total']/stats['count']) for name, stats in points_given.items() if stats['count'] >= 10]
for name, avg in sorted(generous_voters, key=lambda x: x[1], reverse=True)[:5]:
    print(f"{name}: {avg:.2f} average points per vote")

print(f"\n😤 MOST CRITICAL VOTERS (Lowest Average Points Given)")
for name, avg in sorted(generous_voters, key=lambda x: x[1])[:5]:
    print(f"{name}: {avg:.2f} average points per vote")

# Genre Analysis (based on artist patterns)
genre_indicators = {
    'Country': ['Alabama', 'Tyler Childers', 'Chris Stapleton', 'Sturgill Simpson'],
    'Classic Rock': ['Led Zeppelin', 'The Doors', 'Eagles', 'Rolling Stones', 'Pink Floyd'],
    'Jazz/Fusion': ['George Benson', 'Jean-Luc Ponty', 'DAVID GRISMAN QUINTET'],
    'Hip-Hop/R&B': ['Frank Ocean', 'Anderson .Paak', 'The Notorious B.I.G.', 'Mac Miller'],
    'Electronic': ['Daft Punk', 'KAYTRANADA', 'Flying Lotus'],
    'Indie/Alternative': ['My Morning Jacket', 'Pinegrove', 'Father John Misty']
}

print(f"\n🎭 GENRE ANALYSIS")
member_genres = defaultdict(lambda: defaultdict(int))

for sub in submissions:
    submitter_name = id_to_name.get(sub['Submitter ID'], sub['Submitter ID'])
    artist = sub['Artist(s)']
    
    for genre, artists in genre_indicators.items():
        if any(indicator in artist for indicator in artists):
            member_genres[submitter_name][genre] += 1

for member_name in CORE_MEMBERS.values():
    if member_name in member_genres:
        print(f"\n{member_name}'s Genre Distribution:")
        for genre, count in sorted(member_genres[member_name].items(), key=lambda x: x[1], reverse=True):
            print(f"   {genre}: {count} submissions")

print(f"\n🎯 RECOMMENDED VISUALIZATIONS")
print("1. Radar chart of core members' average points received vs given")
print("2. Timeline of submission patterns by round")  
print("3. Vote distribution heatmap (voter vs submitter)")
print("4. Genre diversity chart by member")
print("5. Controversy index bubble chart (variance vs average score)")
print("6. Head-to-head voting matrix for core members")
print("7. 'Hot streak' line chart showing consecutive high-scoring submissions")

print(f"\n🎪 FUN INSIGHTS")
print("• Dylan Graves' comments are legendary - check out his review philosophy!")
print("• The 'Dongle Japes Theme Song' submission is peak meta content")
print("• Ray Charles 'America the Beautiful' got the longest comment defending the choice")
print("• Stephen McCreary's signature 'oh yeah' comments are iconic")
print("• Chris Manning bringing in some deep cuts with international flair")

print(f"\n🏁 ANALYSIS COMPLETE")
print("Data reveals rich patterns in The Dongle Japes' musical tastes and voting behaviors!")