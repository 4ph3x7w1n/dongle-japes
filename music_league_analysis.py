#!/usr/bin/env python3
"""
Music League Analysis for The Dongle Japes
Analyzes CSV data to generate comprehensive statistics and insights
"""

import csv
from collections import defaultdict, Counter
import statistics
import json

# Core Dongle Japes members to focus on
DONGLE_MEMBERS = {
    '201cc8e3af8249c5ba57f2e8d6235fb2': 'Chris Manning',
    '529211ec9c42438f9162e38917f2eeef': 'Max Voorhees', 
    'a83252ecd5dc459cb6e13d5bd395c0a8': 'adamhudzik55',
    'd45b3a6a10ba40218745e3fe18f0d4b8': 'Dylan Graves'
}

def load_data():
    """Load all CSV files into data structures"""
    
    # Load competitors
    competitors = {}
    with open('/mnt/e/Projects/dongle/stuff/competitors.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            competitors[row['ID']] = row['Name']
    
    # Load rounds
    rounds = {}
    with open('/mnt/e/Projects/dongle/stuff/rounds.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rounds[row['ID']] = {
                'name': row['Name'],
                'description': row['Description'],
                'created': row['Created']
            }
    
    # Load submissions
    submissions = []
    with open('/mnt/e/Projects/dongle/stuff/submissions.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            submissions.append(row)
    
    # Load votes
    votes = []
    with open('/mnt/e/Projects/dongle/stuff/votes.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            votes.append(row)
    
    return competitors, rounds, submissions, votes

def calculate_member_stats(competitors, rounds, submissions, votes):
    """Calculate comprehensive stats for each Dongle member"""
    
    member_stats = {}
    
    for member_id, member_name in DONGLE_MEMBERS.items():
        stats = {
            'name': member_name,
            'total_points_received': 0,
            'total_points_given': 0,
            'submissions_count': 0,
            'rounds_participated': set(),
            'best_songs': [],
            'worst_songs': [],
            'round_performance': {},
            'voting_patterns': {},
            'submission_details': []
        }
        
        # Calculate points received (from their submissions)
        member_submissions = [s for s in submissions if s['Submitter ID'] == member_id]
        stats['submissions_count'] = len(member_submissions)
        
        for submission in member_submissions:
            song_votes = [v for v in votes if v['Spotify URI'] == submission['Spotify URI']]
            total_points = sum(int(v['Points Assigned']) for v in song_votes)
            
            song_info = {
                'title': submission['Title'],
                'artist': submission['Artist(s)'],
                'album': submission['Album'],
                'round': rounds[submission['Round ID']]['name'],
                'points': total_points,
                'votes': len(song_votes),
                'comment': submission.get('Comment', ''),
                'spotify_uri': submission['Spotify URI']
            }
            
            stats['submission_details'].append(song_info)
            stats['total_points_received'] += total_points
            stats['rounds_participated'].add(submission['Round ID'])
            
            # Track performance by round
            round_name = rounds[submission['Round ID']]['name']
            if round_name not in stats['round_performance']:
                stats['round_performance'][round_name] = []
            stats['round_performance'][round_name].append(total_points)
        
        # Sort songs by points for best/worst
        stats['submission_details'].sort(key=lambda x: x['points'], reverse=True)
        stats['best_songs'] = stats['submission_details'][:3]
        stats['worst_songs'] = stats['submission_details'][-3:]
        
        # Calculate points given (from their votes)
        member_votes = [v for v in votes if v['Voter ID'] == member_id]
        stats['total_points_given'] = sum(int(v['Points Assigned']) for v in member_votes)
        
        # Voting patterns
        voting_distribution = Counter(int(v['Points Assigned']) for v in member_votes)
        stats['voting_patterns'] = dict(voting_distribution)
        
        member_stats[member_id] = stats
    
    return member_stats

def find_controversial_songs(submissions, votes):
    """Find songs with the biggest vote spreads (most controversial)"""
    
    song_spreads = []
    
    for submission in submissions:
        song_votes = [v for v in votes if v['Spotify URI'] == submission['Spotify URI']]
        if len(song_votes) > 1:
            points = [int(v['Points Assigned']) for v in song_votes]
            spread = max(points) - min(points)
            
            song_spreads.append({
                'title': submission['Title'],
                'artist': submission['Artist(s)'],
                'submitter': submission['Submitter ID'],
                'spread': spread,
                'max_vote': max(points),
                'min_vote': min(points),
                'total_points': sum(points),
                'vote_count': len(points),
                'votes': points
            })
    
    return sorted(song_spreads, key=lambda x: x['spread'], reverse=True)

def find_consensus_picks(submissions, votes):
    """Find songs where everyone voted high (consensus favorites)"""
    
    consensus_songs = []
    
    for submission in submissions:
        song_votes = [v for v in votes if v['Spotify URI'] == submission['Spotify URI']]
        if len(song_votes) >= 4:  # At least 4 votes
            points = [int(v['Points Assigned']) for v in song_votes]
            avg_score = statistics.mean(points)
            min_score = min(points)
            
            if avg_score >= 3.0 and min_score >= 2:  # High average, no very low scores
                consensus_songs.append({
                    'title': submission['Title'],
                    'artist': submission['Artist(s)'],
                    'submitter': submission['Submitter ID'],
                    'avg_score': avg_score,
                    'min_score': min_score,
                    'total_points': sum(points),
                    'vote_count': len(points),
                    'votes': points
                })
    
    return sorted(consensus_songs, key=lambda x: x['avg_score'], reverse=True)

def analyze_round_themes(rounds, submissions, votes):
    """Analyze performance and patterns by round theme"""
    
    round_analysis = {}
    
    for round_id, round_info in rounds.items():
        round_submissions = [s for s in submissions if s['Round ID'] == round_id]
        round_votes = [v for v in votes if any(s['Spotify URI'] == v['Spotify URI'] for s in round_submissions)]
        
        if round_submissions:
            # Calculate stats for this round
            total_songs = len(round_submissions)
            total_votes = len(round_votes)
            
            # Get points distribution
            song_points = {}
            for submission in round_submissions:
                song_votes = [v for v in votes if v['Spotify URI'] == submission['Spotify URI']]
                total_points = sum(int(v['Points Assigned']) for v in song_votes)
                song_points[submission['Spotify URI']] = {
                    'points': total_points,
                    'title': submission['Title'],
                    'artist': submission['Artist(s)'],
                    'submitter': submission['Submitter ID']
                }
            
            # Find winner
            winner_uri = max(song_points.keys(), key=lambda x: song_points[x]['points'])
            winner = song_points[winner_uri]
            
            round_analysis[round_id] = {
                'name': round_info['name'],
                'description': round_info['description'],
                'total_songs': total_songs,
                'total_votes': total_votes,
                'winner': winner,
                'all_songs': list(song_points.values()),
                'dongle_participants': [s['Submitter ID'] for s in round_submissions if s['Submitter ID'] in DONGLE_MEMBERS]
            }
    
    return round_analysis

def generate_fun_stats(competitors, rounds, submissions, votes, member_stats):
    """Generate fun and interesting statistics"""
    
    fun_stats = {}
    
    # Most active submitter
    submission_counts = Counter(s['Submitter ID'] for s in submissions)
    most_active_id = submission_counts.most_common(1)[0][0]
    fun_stats['most_active_submitter'] = {
        'name': competitors.get(most_active_id, 'Unknown'),
        'submissions': submission_counts[most_active_id]
    }
    
    # Most generous voter (gives highest average points)
    voter_generosity = {}
    for vote in votes:
        voter_id = vote['Voter ID']
        if voter_id not in voter_generosity:
            voter_generosity[voter_id] = []
        voter_generosity[voter_id].append(int(vote['Points Assigned']))
    
    avg_generosity = {voter: statistics.mean(points) for voter, points in voter_generosity.items() if len(points) > 5}
    most_generous_id = max(avg_generosity.keys(), key=lambda x: avg_generosity[x])
    fun_stats['most_generous_voter'] = {
        'name': competitors.get(most_generous_id, 'Unknown'),
        'avg_points_given': round(avg_generosity[most_generous_id], 2)
    }
    
    # Most critical voter (gives lowest average points)
    most_critical_id = min(avg_generosity.keys(), key=lambda x: avg_generosity[x])
    fun_stats['most_critical_voter'] = {
        'name': competitors.get(most_critical_id, 'Unknown'),
        'avg_points_given': round(avg_generosity[most_critical_id], 2)
    }
    
    # Dongle member rankings by total points received
    dongle_rankings = []
    for member_id, stats in member_stats.items():
        if stats['submissions_count'] > 0:
            avg_points = stats['total_points_received'] / stats['submissions_count']
            dongle_rankings.append({
                'name': stats['name'],
                'total_points': stats['total_points_received'],
                'submissions': stats['submissions_count'],
                'avg_points_per_song': round(avg_points, 2)
            })
    
    dongle_rankings.sort(key=lambda x: x['total_points'], reverse=True)
    fun_stats['dongle_rankings'] = dongle_rankings
    
    return fun_stats

def main():
    """Main analysis function"""
    
    print("Loading Music League data...")
    competitors, rounds, submissions, votes = load_data()
    
    print("Calculating member statistics...")
    member_stats = calculate_member_stats(competitors, rounds, submissions, votes)
    
    print("Finding controversial songs...")
    controversial = find_controversial_songs(submissions, votes)
    
    print("Finding consensus picks...")
    consensus = find_consensus_picks(submissions, votes)
    
    print("Analyzing round themes...")
    round_analysis = analyze_round_themes(rounds, submissions, votes)
    
    print("Generating fun statistics...")
    fun_stats = generate_fun_stats(competitors, rounds, submissions, votes, member_stats)
    
    # Generate comprehensive report
    print("\n" + "="*80)
    print("THE DONGLE JAPES MUSIC LEAGUE ANALYSIS")
    print("="*80)
    
    # Member Rankings
    print("\n🏆 DONGLE JAPES LEADERBOARD")
    print("-" * 40)
    for i, member in enumerate(fun_stats['dongle_rankings'], 1):
        print(f"{i}. {member['name']}: {member['total_points']} points ({member['submissions']} songs, {member['avg_points_per_song']} avg)")
    
    # Individual Member Analysis
    print("\n👤 INDIVIDUAL MEMBER BREAKDOWN")
    print("-" * 40)
    for member_id, stats in member_stats.items():
        print(f"\n{stats['name']}:")
        print(f"  • Total Points Received: {stats['total_points_received']}")
        print(f"  • Songs Submitted: {stats['submissions_count']}")
        print(f"  • Rounds Participated: {len(stats['rounds_participated'])}")
        
        if stats['best_songs']:
            print(f"  • Best Song: \"{stats['best_songs'][0]['title']}\" by {stats['best_songs'][0]['artist']} ({stats['best_songs'][0]['points']} points)")
        
        if len(stats['worst_songs']) > 0 and stats['worst_songs'][-1]['points'] < stats['best_songs'][0]['points']:
            print(f"  • Struggled With: \"{stats['worst_songs'][-1]['title']}\" by {stats['worst_songs'][-1]['artist']} ({stats['worst_songs'][-1]['points']} points)")
    
    # Most Controversial Songs
    print("\n🔥 MOST CONTROVERSIAL SONGS")
    print("-" * 40)
    for i, song in enumerate(controversial[:5], 1):
        submitter_name = competitors.get(song['submitter'], 'Unknown')
        print(f"{i}. \"{song['title']}\" by {song['artist']}")
        print(f"   Submitted by: {submitter_name}")
        print(f"   Vote spread: {song['min_vote']}-{song['max_vote']} (spread of {song['spread']})")
        print(f"   Total points: {song['total_points']}")
        print()
    
    # Consensus Picks
    print("\n🎯 CONSENSUS FAVORITES")
    print("-" * 40)
    for i, song in enumerate(consensus[:5], 1):
        submitter_name = competitors.get(song['submitter'], 'Unknown')
        print(f"{i}. \"{song['title']}\" by {song['artist']}")
        print(f"   Submitted by: {submitter_name}")
        print(f"   Average score: {song['avg_score']:.2f}")
        print(f"   Total points: {song['total_points']}")
        print()
    
    # Round Winners
    print("\n🏅 ROUND WINNERS")
    print("-" * 40)
    for round_id, analysis in round_analysis.items():
        winner = analysis['winner']
        submitter_name = competitors.get(winner['submitter'], 'Unknown')
        print(f"{analysis['name']}: \"{winner['title']}\" by {winner['artist']}")
        print(f"   Submitted by: {submitter_name} ({winner['points']} points)")
        print()
    
    # Fun Stats
    print("\n📊 INTERESTING STATS")
    print("-" * 40)
    print(f"Most Active Submitter: {fun_stats['most_active_submitter']['name']} ({fun_stats['most_active_submitter']['submissions']} songs)")
    print(f"Most Generous Voter: {fun_stats['most_generous_voter']['name']} (avg {fun_stats['most_generous_voter']['avg_points_given']} points)")
    print(f"Most Critical Voter: {fun_stats['most_critical_voter']['name']} (avg {fun_stats['most_critical_voter']['avg_points_given']} points)")
    
    # Round Themes Analysis
    print("\n🎵 ROUND THEMES BREAKDOWN")
    print("-" * 40)
    for round_id, analysis in round_analysis.items():
        print(f"\n{analysis['name']}")
        print(f"  Theme: {analysis['description']}")
        print(f"  Total submissions: {analysis['total_songs']}")
        print(f"  Dongle participation: {len(analysis['dongle_participants'])}/4 members")
        winner = analysis['winner']
        print(f"  Winner: \"{winner['title']}\" by {winner['artist']} ({winner['points']} points)")
    
    print("\n" + "="*80)
    print("Analysis complete! 🎵")

if __name__ == "__main__":
    main()