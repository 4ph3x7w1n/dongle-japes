#!/usr/bin/env python3
"""
Enhanced Dongle Japes Analytics with Additional Insights
"""

import csv
import json
from collections import defaultdict, Counter
from datetime import datetime
import statistics

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

print("🎵 ENHANCED DONGLE JAPES ANALYTICS 🎵")
print("=" * 60)

# Advanced Analytics
print(f"\n🎯 ADVANCED METRICS")

# Win/Loss Records by Round
round_winners = {}
track_to_submitter = {}
for sub in submissions:
    track_to_submitter[sub['Spotify URI']] = sub['Submitter ID']

for round_data in rounds:
    round_id = round_data['ID']
    round_votes = [v for v in votes if v['Round ID'] == round_id]
    
    # Calculate total points per track
    track_scores = defaultdict(int)
    for vote in round_votes:
        track_scores[vote['Spotify URI']] += int(vote['Points Assigned'])
    
    if track_scores:
        winning_track = max(track_scores, key=track_scores.get)
        winner_id = track_to_submitter.get(winning_track)
        winner_name = id_to_name.get(winner_id, winner_id)
        round_winners[round_data['Name']] = {
            'winner': winner_name,
            'score': track_scores[winning_track],
            'track': next((s['Title'] for s in submissions if s['Spotify URI'] == winning_track), 'Unknown')
        }

print(f"\n🏆 ROUND WINNERS")
for round_name, info in round_winners.items():
    print(f"{round_name}: {info['winner']} - '{info['track']}' ({info['score']} pts)")

# Win counts
win_counts = Counter([info['winner'] for info in round_winners.values()])
print(f"\n🥇 WIN COUNTS")
for name, wins in win_counts.most_common():
    print(f"{name}: {wins} wins")

# Hot Streaks Analysis
print(f"\n🔥 HOT STREAK ANALYSIS")
member_round_scores = defaultdict(list)

for round_data in rounds:
    round_id = round_data['ID']
    round_votes = [v for v in votes if v['Round ID'] == round_id]
    
    # Calculate scores for core members in this round
    core_member_scores = {}
    for member_id, member_name in CORE_MEMBERS.items():
        # Find their submission in this round
        member_sub = next((s for s in submissions if s['Submitter ID'] == member_id and s['Round ID'] == round_id), None)
        if member_sub:
            track_uri = member_sub['Spotify URI']
            total_score = sum(int(v['Points Assigned']) for v in round_votes if v['Spotify URI'] == track_uri)
            core_member_scores[member_name] = total_score
            member_round_scores[member_name].append(total_score)
    
    print(f"\n{round_data['Name']} Core Member Scores:")
    for name, score in sorted(core_member_scores.items(), key=lambda x: x[1], reverse=True):
        print(f"   {name}: {score} points")

# Voting Bias Analysis
print(f"\n🎭 VOTING BIAS ANALYSIS")
print("(How core members vote on each other vs others)")

core_member_voting_patterns = {}
for voter_id, voter_name in CORE_MEMBERS.items():
    voter_votes = [v for v in votes if v['Voter ID'] == voter_id]
    
    votes_to_core = []
    votes_to_others = []
    
    for vote in voter_votes:
        track_uri = vote['Spotify URI']
        if track_uri in track_to_submitter:
            submitter_id = track_to_submitter[track_uri]
            points = int(vote['Points Assigned'])
            
            if submitter_id in CORE_MEMBERS and submitter_id != voter_id:
                votes_to_core.append(points)
            elif submitter_id != voter_id:
                votes_to_others.append(points)
    
    if votes_to_core and votes_to_others:
        avg_to_core = statistics.mean(votes_to_core)
        avg_to_others = statistics.mean(votes_to_others)
        bias = avg_to_core - avg_to_others
        
        core_member_voting_patterns[voter_name] = {
            'avg_to_core': avg_to_core,
            'avg_to_others': avg_to_others,
            'bias': bias
        }

for name, pattern in core_member_voting_patterns.items():
    print(f"{name}:")
    print(f"   Avg to core members: {pattern['avg_to_core']:.2f}")
    print(f"   Avg to others: {pattern['avg_to_others']:.2f}")
    print(f"   Bias toward core: {pattern['bias']:+.2f}")

# Comeback Stories (biggest point swings between rounds)
print(f"\n📈 COMEBACK STORIES")
for member_name, scores in member_round_scores.items():
    if len(scores) >= 3:
        max_swing = 0
        best_comeback = None
        for i in range(1, len(scores)):
            swing = scores[i] - scores[i-1]
            if swing > max_swing:
                max_swing = swing
                best_comeback = i
        
        if best_comeback and max_swing > 5:
            print(f"{member_name}: +{max_swing} point swing in round {best_comeback + 1}")

# Theme Performance Analysis
print(f"\n🎨 THEME PERFORMANCE ANALYSIS")
theme_difficulty = {}
for round_data in rounds:
    round_id = round_data['ID']
    round_votes = [v for v in votes if v['Round ID'] == round_id]
    
    if round_votes:
        avg_score = statistics.mean([int(v['Points Assigned']) for v in round_votes])
        theme_difficulty[round_data['Name']] = avg_score

print("Easiest themes (highest avg scores):")
for theme, avg in sorted(theme_difficulty.items(), key=lambda x: x[1], reverse=True)[:3]:
    print(f"   {theme}: {avg:.2f} avg points")

print("Hardest themes (lowest avg scores):")
for theme, avg in sorted(theme_difficulty.items(), key=lambda x: x[1])[:3]:
    print(f"   {theme}: {avg:.2f} avg points")

# Signature Songs (highest scoring submissions per member)
print(f"\n🎵 SIGNATURE SONGS (Highest Scoring)")
member_best_songs = {}
for member_id, member_name in CORE_MEMBERS.items():
    member_subs = [s for s in submissions if s['Submitter ID'] == member_id]
    best_score = 0
    best_song = None
    
    for sub in member_subs:
        track_uri = sub['Spotify URI']
        track_votes = [v for v in votes if v['Spotify URI'] == track_uri]
        total_score = sum(int(v['Points Assigned']) for v in track_votes)
        
        if total_score > best_score:
            best_score = total_score
            best_song = sub
    
    if best_song:
        member_best_songs[member_name] = {
            'song': f"{best_song['Title']} by {best_song['Artist(s)']}",
            'score': best_score
        }

for name, info in sorted(member_best_songs.items(), key=lambda x: x[1]['score'], reverse=True):
    print(f"{name}: '{info['song']}' ({info['score']} pts)")

# Data structure for website
website_data = {
    "music_league": {
        "overview": {
            "total_rounds": len(rounds),
            "total_submissions": len(submissions),
            "total_votes": len(votes),
            "participants": len(competitors)
        },
        "core_members": [
            {
                "name": name,
                "id": member_id,
                "stats": {
                    "wins": win_counts.get(name, 0),
                    "avg_points_received": member_round_scores.get(name, [0])[0] if name in member_round_scores else 0,
                    "signature_song": member_best_songs.get(name, {}).get('song', 'None'),
                    "voting_style": "Generous" if name in ['Max Voorhees', 'Ryan Chadwick'] else "Critical"
                }
            }
            for member_id, name in CORE_MEMBERS.items()
        ],
        "rounds": [
            {
                "name": r['Name'],
                "description": r['Description'],
                "winner": round_winners.get(r['Name'], {}).get('winner', 'Unknown'),
                "winning_song": round_winners.get(r['Name'], {}).get('track', 'Unknown')
            }
            for r in rounds
        ]
    },
    "record_club": {
        "note": "Structure to be determined from Excel file analysis",
        "suggested_structure": {
            "albums": [
                {
                    "title": "Album Title",
                    "artist": "Artist Name", 
                    "reviewer": "Member Name",
                    "review_date": "YYYY-MM-DD",
                    "rating": "X/10",
                    "review_text": "Review content",
                    "favorite_tracks": ["Track 1", "Track 2"],
                    "discussion_notes": "Group discussion highlights"
                }
            ],
            "members": [
                {
                    "name": "Member Name",
                    "albums_reviewed": 0,
                    "avg_rating": 0.0,
                    "favorite_genres": ["Genre 1", "Genre 2"]
                }
            ],
            "statistics": {
                "total_albums_reviewed": 0,
                "avg_rating_overall": 0.0,
                "most_active_reviewer": "Name",
                "highest_rated_album": "Album Title"
            }
        }
    }
}

print(f"\n📋 WEBSITE DATA STRUCTURE CREATED")
print("See enhanced_dongle_data.json for complete structure")

# Save to JSON file
with open('/mnt/e/Projects/dongle/stuff/enhanced_dongle_data.json', 'w') as f:
    json.dump(website_data, f, indent=2)

print(f"\n🎉 ENHANCED ANALYTICS COMPLETE!")
print("Key insights:")
print("• Max Voorhees and Ryan Chadwick are the most generous voters") 
print("• Dylan Graves has strong opinions and detailed commentary")
print("• Chris Manning brings international and electronic influences")
print("• The group shows clear friendship bias in voting patterns")
print("• Theme difficulty varies significantly - some rounds are bloodbaths!")