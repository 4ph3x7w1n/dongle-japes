#!/usr/bin/env python3
"""
Enhanced Dongle Japes Music League Insights
Creates fun, detailed statistics perfect for the website
"""

import csv
from collections import defaultdict, Counter
import statistics

# Core Dongle Japes members
DONGLE_MEMBERS = {
    '201cc8e3af8249c5ba57f2e8d6235fb2': 'Chris Manning',
    '529211ec9c42438f9162e38917f2eeef': 'Max Voorhees', 
    'a83252ecd5dc459cb6e13d5bd395c0a8': 'adamhudzik55',
    'd45b3a6a10ba40218745e3fe18f0d4b8': 'Dylan Graves'
}

def load_data():
    """Load all CSV files"""
    competitors = {}
    with open('/mnt/e/Projects/dongle/stuff/competitors.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            competitors[row['ID']] = row['Name']
    
    rounds = {}
    with open('/mnt/e/Projects/dongle/stuff/rounds.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rounds[row['ID']] = {
                'name': row['Name'],
                'description': row['Description'],
                'created': row['Created']
            }
    
    submissions = []
    with open('/mnt/e/Projects/dongle/stuff/submissions.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            submissions.append(row)
    
    votes = []
    with open('/mnt/e/Projects/dongle/stuff/votes.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            votes.append(row)
    
    return competitors, rounds, submissions, votes

def get_detailed_member_analysis():
    """Generate detailed analysis for each Dongle member"""
    competitors, rounds, submissions, votes = load_data()
    
    detailed_analysis = {}
    
    for member_id, member_name in DONGLE_MEMBERS.items():
        member_submissions = [s for s in submissions if s['Submitter ID'] == member_id]
        
        # Skip if no submissions
        if not member_submissions:
            detailed_analysis[member_name] = {
                'status': 'MIA',
                'note': 'No submissions found - probably too busy being awesome'
            }
            continue
        
        # Calculate detailed stats
        song_performances = []
        total_points = 0
        round_wins = 0
        
        for submission in member_submissions:
            song_votes = [v for v in votes if v['Spotify URI'] == submission['Spotify URI']]
            song_points = sum(int(v['Points Assigned']) for v in song_votes)
            
            # Check if this won the round
            round_submissions = [s for s in submissions if s['Round ID'] == submission['Round ID']]
            round_max_points = 0
            for round_sub in round_submissions:
                round_votes = [v for v in votes if v['Spotify URI'] == round_sub['Spotify URI']]
                round_sub_points = sum(int(v['Points Assigned']) for v in round_votes)
                round_max_points = max(round_max_points, round_sub_points)
            
            is_winner = song_points == round_max_points and song_points > 0
            if is_winner:
                round_wins += 1
            
            song_performances.append({
                'title': submission['Title'],
                'artist': submission['Artist(s)'],
                'album': submission['Album'],
                'round': rounds[submission['Round ID']]['name'],
                'points': song_points,
                'votes_count': len(song_votes),
                'is_winner': is_winner,
                'comment': submission.get('Comment', ''),
                'individual_votes': [int(v['Points Assigned']) for v in song_votes]
            })
            
            total_points += song_points
        
        # Sort by points
        song_performances.sort(key=lambda x: x['points'], reverse=True)
        
        # Calculate voting patterns when this member votes
        member_votes = [v for v in votes if v['Voter ID'] == member_id]
        voting_generosity = statistics.mean([int(v['Points Assigned']) for v in member_votes]) if member_votes else 0
        
        # Find genre patterns
        genres = []
        for perf in song_performances:
            if 'rock' in perf['artist'].lower() or 'rock' in perf['album'].lower():
                genres.append('Rock')
            elif any(word in perf['artist'].lower() for word in ['jazz', 'blues', 'soul']):
                genres.append('Jazz/Blues/Soul')
            elif any(word in perf['artist'].lower() for word in ['hip', 'hop', 'rap']):
                genres.append('Hip-Hop')
            elif any(word in perf['artist'].lower() for word in ['electronic', 'house', 'techno']):
                genres.append('Electronic')
            else:
                genres.append('Other')
        
        genre_preference = Counter(genres).most_common(1)[0][0] if genres else 'Eclectic'
        
        detailed_analysis[member_name] = {
            'total_points': total_points,
            'total_submissions': len(member_submissions),
            'average_points': round(total_points / len(member_submissions), 2),
            'round_wins': round_wins,
            'win_rate': round((round_wins / len(member_submissions)) * 100, 1),
            'voting_generosity': round(voting_generosity, 2),
            'best_performance': song_performances[0],
            'worst_performance': song_performances[-1],
            'all_songs': song_performances,
            'dominant_genre': genre_preference,
            'consistency_score': round(statistics.stdev([p['points'] for p in song_performances]), 2) if len(song_performances) > 1 else 0
        }
    
    return detailed_analysis

def create_fun_insights():
    """Generate fun, quirky insights for the website"""
    competitors, rounds, submissions, votes = load_data()
    
    insights = []
    
    # Find the most commented song
    most_commented = max(submissions, key=lambda x: len(x.get('Comment', '')))
    if most_commented.get('Comment'):
        insights.append({
            'title': "Most Passionate Submission",
            'content': f'"{most_commented["Title"]}" by {most_commented["Artist(s)"]} came with a {len(most_commented["Comment"])} character essay. The dedication is real.',
            'submitter': competitors.get(most_commented['Submitter ID'], 'Unknown')
        })
    
    # Find 5-point votes (perfect scores)
    perfect_votes = [v for v in votes if v['Points Assigned'] == '5']
    perfect_vote_counts = Counter(v['Spotify URI'] for v in perfect_votes)
    
    if perfect_vote_counts:
        most_perfect_uri = perfect_vote_counts.most_common(1)[0][0]
        most_perfect_song = next(s for s in submissions if s['Spotify URI'] == most_perfect_uri)
        perfect_count = perfect_vote_counts[most_perfect_uri]
        
        insights.append({
            'title': "Most 5-Star Reviews",
            'content': f'"{most_perfect_song["Title"]}" by {most_perfect_song["Artist(s)"]} got {perfect_count} perfect 5-point votes. Absolute banger confirmed.',
            'submitter': competitors.get(most_perfect_song['Submitter ID'], 'Unknown')
        })
    
    # Find 0-point votes (harsh reviews)
    zero_votes = [v for v in votes if v['Points Assigned'] == '0']
    zero_vote_counts = Counter(v['Spotify URI'] for v in zero_votes)
    
    if zero_vote_counts:
        most_zero_uri = zero_vote_counts.most_common(1)[0][0]
        most_zero_song = next(s for s in submissions if s['Spotify URI'] == most_zero_uri)
        zero_count = zero_vote_counts[most_zero_uri]
        
        insights.append({
            'title': "Most Controversial (0-Point Magnet)",
            'content': f'"{most_zero_song["Title"]}" by {most_zero_song["Artist(s)"]} received {zero_count} zero-point votes. Either love it or hate it.',
            'submitter': competitors.get(most_zero_song['Submitter ID'], 'Unknown')
        })
    
    # Find Dylan's comments (he seems to write detailed reviews)
    dylan_id = 'd45b3a6a10ba40218745e3fe18f0d4b8'
    dylan_votes = [v for v in votes if v['Voter ID'] == dylan_id and v.get('Comment')]
    
    if dylan_votes:
        total_comment_length = sum(len(v.get('Comment', '')) for v in dylan_votes)
        insights.append({
            'title': "Dylan's Novel-Length Reviews",
            'content': f"Dylan wrote {total_comment_length} characters worth of voting comments. That's like {total_comment_length // 250} paragraphs of pure music criticism.",
            'submitter': 'Dylan Graves'
        })
    
    # Check Chris Manning's self-submission success
    chris_id = '201cc8e3af8249c5ba57f2e8d6235fb2'
    dongle_theme_song = next((s for s in submissions if 'Dongle Japes Theme Song' in s['Title']), None)
    if dongle_theme_song and dongle_theme_song['Submitter ID'] == chris_id:
        song_votes = [v for v in votes if v['Spotify URI'] == dongle_theme_song['Spotify URI']]
        total_points = sum(int(v['Points Assigned']) for v in song_votes)
        insights.append({
            'title': "Ultimate Self-Promotion",
            'content': f'Chris submitted the literal "Dongle Japes Theme Song" and got {total_points} points for it. The audacity paid off.',
            'submitter': 'Chris Manning'
        })
    
    return insights

def generate_website_content():
    """Generate formatted content perfect for the website"""
    
    print("🎵 THE DONGLE JAPES MUSIC LEAGUE HALL OF FAME 🎵")
    print("=" * 60)
    
    # Get detailed member analysis
    member_analysis = get_detailed_member_analysis()
    
    print("\n🏆 THE CHAMPIONS")
    print("-" * 30)
    
    # Sort members by total points
    ranked_members = [(name, data) for name, data in member_analysis.items() if 'total_points' in data]
    ranked_members.sort(key=lambda x: x[1]['total_points'], reverse=True)
    
    for i, (name, data) in enumerate(ranked_members, 1):
        print(f"\n{i}. {name} - {data['total_points']} Points")
        print(f"   └── {data['total_submissions']} songs • {data['average_points']} avg • {data['round_wins']} wins ({data['win_rate']}%)")
        print(f"   └── Crown Jewel: \"{data['best_performance']['title']}\" ({data['best_performance']['points']} points)")
        print(f"   └── Voting Style: {'Generous' if data['voting_generosity'] > 2.5 else 'Critical'} ({data['voting_generosity']} avg points given)")
        print(f"   └── Genre Preference: {data['dominant_genre']}")
    
    # Check for MIA members
    mia_members = [(name, data) for name, data in member_analysis.items() if 'status' in data]
    if mia_members:
        print("\n😴 MIA MEMBERS")
        print("-" * 30)
        for name, data in mia_members:
            print(f"• {name}: {data['note']}")
    
    # Detailed song breakdowns
    print("\n🎧 COMPLETE SONG BREAKDOWN")
    print("-" * 30)
    
    for name, data in ranked_members:
        print(f"\n{name}'s Complete Catalog:")
        for i, song in enumerate(data['all_songs'], 1):
            winner_emoji = "👑" if song['is_winner'] else ""
            print(f"  {i:2d}. \"{song['title']}\" by {song['artist']} - {song['points']} pts {winner_emoji}")
            print(f"      Round: {song['round']}")
            if song['comment']:
                print(f"      Note: {song['comment'][:100]}{'...' if len(song['comment']) > 100 else ''}")
    
    # Fun insights
    print("\n🔥 FUN INSIGHTS & DISCOVERIES")
    print("-" * 30)
    
    insights = create_fun_insights()
    for insight in insights:
        print(f"\n{insight['title']}:")
        print(f"   {insight['content']}")
        if 'submitter' in insight:
            print(f"   Credit: {insight['submitter']}")
    
    # Round-by-round breakdown
    competitors, rounds, submissions, votes = load_data()
    
    print("\n📅 ROUND-BY-ROUND DONGLE DOMINATION")
    print("-" * 30)
    
    for round_id, round_info in rounds.items():
        round_submissions = [s for s in submissions if s['Round ID'] == round_id]
        dongle_submissions = [s for s in round_submissions if s['Submitter ID'] in DONGLE_MEMBERS]
        
        if dongle_submissions:
            print(f"\n{round_info['name']} - \"{round_info['description']}\"")
            print(f"Dongle Participation: {len(dongle_submissions)}/4 members")
            
            # Find winner and Dongle placements
            all_song_points = {}
            for sub in round_submissions:
                song_votes = [v for v in votes if v['Spotify URI'] == sub['Spotify URI']]
                points = sum(int(v['Points Assigned']) for v in song_votes)
                all_song_points[sub['Spotify URI']] = {
                    'points': points,
                    'title': sub['Title'],
                    'artist': sub['Artist(s)'],
                    'submitter_id': sub['Submitter ID']
                }
            
            # Sort by points
            sorted_songs = sorted(all_song_points.items(), key=lambda x: x[1]['points'], reverse=True)
            
            # Show Dongle member placements
            for i, (uri, song_data) in enumerate(sorted_songs, 1):
                if song_data['submitter_id'] in DONGLE_MEMBERS:
                    member_name = DONGLE_MEMBERS[song_data['submitter_id']]
                    place_emoji = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"#{i}"
                    print(f"   {place_emoji} {member_name}: \"{song_data['title']}\" ({song_data['points']} pts)")

def main():
    generate_website_content()

if __name__ == "__main__":
    main()