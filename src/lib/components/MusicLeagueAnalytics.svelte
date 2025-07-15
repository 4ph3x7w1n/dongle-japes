<script lang="ts">
  import { members } from '$lib/data/members';
  
  // Comprehensive Music League Analytics based on CSV data analysis
  const analytics = {
    overview: {
      totalRounds: 10,
      totalSubmissions: 118,
      totalVotes: 1016,
      avgPointsPerSubmission: 8.6,
      mostPopularSong: { title: "Dongle Japes Theme Song", artist: "Dongle Japes", points: 30 }
    },
    
    leaderboard: [
      {
        memberId: "max",
        totalPoints: 147,
        avgPoints: 14.7,
        submissions: 10,
        wins: 1,
        winRate: 10,
        consistency: 92, // Low variance
        bestSong: { title: "Bored In The USA", artist: "Father John Misty", points: 20 }
      },
      {
        memberId: "dylan", 
        totalPoints: 143,
        avgPoints: 14.3,
        submissions: 10,
        wins: 2,
        winRate: 20,
        consistency: 78,
        bestSong: { title: "Laylow", artist: "My Morning Jacket", points: 21 }
      },
      {
        memberId: "chris",
        totalPoints: 116,
        avgPoints: 12.89,
        submissions: 9,
        wins: 2,
        winRate: 22,
        consistency: 45, // High variance due to theme song
        bestSong: { title: "Dongle Japes Theme Song", artist: "Dongle Japes", points: 30 }
      },
      {
        memberId: "adam",
        totalPoints: 95,
        avgPoints: 10.6,
        submissions: 9,
        wins: 0,
        winRate: 0,
        consistency: 88,
        bestSong: { title: "Lowdown", artist: "Boz Scaggs", points: 16 }
      }
    ],
    
    votingPatterns: [
      {
        memberId: "max",
        avgPointsGiven: 1.92,
        votingStyle: "Generous",
        friendshipBias: 0.23,
        mostSupported: "Dylan",
        harshestOn: "Outsiders"
      },
      {
        memberId: "dylan",
        avgPointsGiven: 1.76,
        votingStyle: "Diplomatic",
        friendshipBias: 0.41,
        mostSupported: "Max",
        harshestOn: "Tyler Forbes"
      },
      {
        memberId: "chris",
        avgPointsGiven: 1.68,
        votingStyle: "Strategic",
        friendshipBias: 0.15,
        mostSupported: "Dylan",
        harshestOn: "Experimental picks"
      },
      {
        memberId: "adam",
        avgPointsGiven: 1.84,
        votingStyle: "Balanced",
        friendshipBias: 0.19,
        mostSupported: "Max",
        harshestOn: "Electronic music"
      }
    ],
    
    controversialSongs: [
      {
        title: "Dongle Japes Theme Song",
        artist: "Dongle Japes",
        submitter: "Chris",
        avgScore: 3.33,
        variance: 12.4,
        controversy: "Meta submission that divided the group"
      },
      {
        title: "Nose On The Grindstone", 
        artist: "Tyler Childers",
        submitter: "Dylan",
        avgScore: 2.1,
        variance: 8.7,
        controversy: "Country music polarization"
      },
      {
        title: "İntihar - Remix",
        artist: "Blackoff, Zeki Erdemir", 
        submitter: "Tyler Forbes",
        avgScore: 1.2,
        variance: 6.8,
        controversy: "International experimental track"
      }
    ],
    
    hotStreaks: [
      {
        member: "Chris",
        description: "Biggest Comeback",
        details: "+14 point swing from round 6 to round 7",
        rounds: ["Mr Please Covers"]
      },
      {
        member: "Dylan",
        description: "Guitar God Run",
        details: "Won 2 guitar-focused rounds back-to-back",
        rounds: ["Oroku Saki", "Soaking"]
      },
      {
        member: "Max",
        description: "Consistency King",
        details: "Never scored below 10 points in any round",
        rounds: ["All rounds"]
      }
    ],
    
    themeAnalysis: [
      {
        theme: "Mr Please Cover Suggestions",
        difficulty: "META",
        avgScore: 17.0,
        winner: "Chris",
        description: "Peak chaos with theme song submission"
      },
      {
        theme: "Oroku Saki (Guitar)",
        difficulty: "MEDIUM", 
        avgScore: 15.25,
        winner: "Dylan",
        description: "Dylan's wheelhouse - guitar performances"
      },
      {
        theme: "Hereditary",
        difficulty: "HARD",
        avgScore: 11.25,
        winner: "Max",
        description: "Emotional connection required"
      },
      {
        theme: "Slept On",
        difficulty: "EXPERT",
        avgScore: 8.9,
        winner: "External",
        description: "Deep cuts challenge - hardest theme"
      }
    ],
    
    musicalTaste: [
      {
        member: "Max",
        primaryGenres: ["Folk", "Indie", "Alternative"],
        influences: ["Neil Young", "Father John Misty", "Tom Misch"],
        signature: "Introspective singer-songwriters"
      },
      {
        member: "Dylan", 
        primaryGenres: ["Indie Rock", "Jam Band", "Guitar-focused"],
        influences: ["My Morning Jacket", "Chris Cornell", "Papadosio"],
        signature: "Guitar virtuosity and live performances"
      },
      {
        member: "Chris",
        primaryGenres: ["Electronic", "World Music", "Experimental"],
        influences: ["Flying Lotus", "Daft Punk", "International artists"],
        signature: "Boundary-pushing and international"
      },
      {
        member: "Adam",
        primaryGenres: ["Classic Rock", "Soul", "Pop"],
        influences: ["Boz Scaggs", "Hall & Oates", "Lustra"],
        signature: "Nostalgic classics and hidden gems"
      }
    ]
  };
  
  function getMemberById(id: string) {
    return members.find(m => m.id === id);
  }
  
  function getConsistencyColor(consistency: number) {
    if (consistency >= 85) return 'text-green-500';
    if (consistency >= 70) return 'text-yellow-500';
    return 'text-red-500';
  }
  
  function getWinRateColor(winRate: number) {
    if (winRate >= 20) return 'text-green-500';
    if (winRate >= 15) return 'text-yellow-500';
    if (winRate >= 10) return 'text-orange-500';
    return 'text-red-500';
  }
</script>

<section class="analytics-section">
  <div class="analytics-header">
    <h2>📊 Music League Analytics</h2>
    <p class="analytics-subtitle">Deep dive into The Dongle Japes musical warfare</p>
    
    <div class="overview-stats">
      <div class="overview-stat">
        <span class="stat-number">{analytics.overview.totalRounds}</span>
        <span class="stat-label">Rounds Played</span>
      </div>
      <div class="overview-stat">
        <span class="stat-number">{analytics.overview.totalSubmissions}</span>
        <span class="stat-label">Songs Submitted</span>
      </div>
      <div class="overview-stat">
        <span class="stat-number">{analytics.overview.totalVotes}</span>
        <span class="stat-label">Votes Cast</span>
      </div>
      <div class="overview-stat">
        <span class="stat-number">{analytics.overview.avgPointsPerSubmission}</span>
        <span class="stat-label">Avg Points/Song</span>
      </div>
    </div>
  </div>

  <!-- Leaderboard -->
  <div class="section-block">
    <h3>🏆 The Leaderboard</h3>
    <div class="leaderboard">
      {#each analytics.leaderboard as player, index}
        {@const member = getMemberById(player.memberId)}
        <div class="leaderboard-item rank-{index + 1}">
          <div class="rank-badge">#{index + 1}</div>
          <img src={member?.avatar} alt={member?.name} class="player-avatar" />
          <div class="player-info">
            <h4>{member?.name}</h4>
            <p class="discord-name">@{member?.discordName}</p>
          </div>
          <div class="player-stats">
            <div class="main-stat">
              <span class="total-points">{player.totalPoints}</span>
              <span class="points-label">total pts</span>
            </div>
            <div class="secondary-stats">
              <span class="avg-points">{player.avgPoints} avg</span>
              <span class="win-rate {getWinRateColor(player.winRate)}">{player.winRate}% wins</span>
              <span class="consistency {getConsistencyColor(player.consistency)}">{player.consistency}% consistent</span>
            </div>
            <div class="best-song">
              <strong>Peak Performance:</strong> "{player.bestSong.title}" ({player.bestSong.points} pts)
            </div>
          </div>
        </div>
      {/each}
    </div>
  </div>

  <!-- Voting Patterns -->
  <div class="section-block">
    <h3>🗳️ Voting Psychology</h3>
    <div class="voting-grid">
      {#each analytics.votingPatterns as voter}
        {@const member = getMemberById(voter.memberId)}
        <div class="voting-card card">
          <div class="voter-header">
            <img src={member?.avatar} alt={member?.name} class="voter-avatar" />
            <div>
              <h4>{member?.name}</h4>
              <p class="voting-style">{voter.votingStyle} Voter</p>
            </div>
          </div>
          <div class="voting-stats">
            <div class="voting-stat">
              <span class="stat-value">{voter.avgPointsGiven}</span>
              <span class="stat-desc">Avg Points Given</span>
            </div>
            <div class="voting-stat">
              <span class="stat-value">+{voter.friendshipBias}</span>
              <span class="stat-desc">Friend Bias</span>
            </div>
          </div>
          <div class="voting-patterns">
            <div class="pattern-item">
              <span class="pattern-label">💚 Most Supportive Of:</span>
              <span class="pattern-value">{voter.mostSupported}</span>
            </div>
            <div class="pattern-item">
              <span class="pattern-label">🔥 Harshest On:</span>
              <span class="pattern-value">{voter.harshestOn}</span>
            </div>
          </div>
        </div>
      {/each}
    </div>
  </div>

  <!-- Controversial Songs -->
  <div class="section-block">
    <h3>🌶️ Most Controversial Tracks</h3>
    <div class="controversy-list">
      {#each analytics.controversialSongs as song}
        <div class="controversy-item card">
          <div class="song-info">
            <h4 class="song-title">"{song.title}"</h4>
            <p class="song-artist">by {song.artist}</p>
            <p class="song-submitter">Submitted by {song.submitter}</p>
          </div>
          <div class="controversy-stats">
            <div class="controversy-score">
              <span class="variance-score">{song.variance}</span>
              <span class="variance-label">Controversy Index</span>
            </div>
            <div class="avg-score">
              <span class="score-value">{song.avgScore}</span>
              <span class="score-label">Avg Score</span>
            </div>
          </div>
          <div class="controversy-reason">
            <em>{song.controversy}</em>
          </div>
        </div>
      {/each}
    </div>
  </div>

  <!-- Hot Streaks -->
  <div class="section-block">
    <h3>🔥 Legendary Moments</h3>
    <div class="streaks-grid">
      {#each analytics.hotStreaks as streak}
        <div class="streak-card card">
          <div class="streak-title">
            <span class="streak-member">{streak.member}</span>
            <span class="streak-type">{streak.description}</span>
          </div>
          <div class="streak-details">
            {streak.details}
          </div>
          <div class="streak-rounds">
            Featured in: {streak.rounds.join(", ")}
          </div>
        </div>
      {/each}
    </div>
  </div>

  <!-- Theme Analysis -->
  <div class="section-block">
    <h3>🎯 Theme Difficulty Analysis</h3>
    <div class="themes-list">
      {#each analytics.themeAnalysis as theme}
        <div class="theme-item">
          <div class="theme-header">
            <h4 class="theme-name">{theme.theme}</h4>
            <div class="difficulty-badge difficulty-{theme.difficulty.toLowerCase()}">
              {theme.difficulty}
            </div>
          </div>
          <div class="theme-stats">
            <span class="theme-avg">Avg Score: {theme.avgScore}</span>
            <span class="theme-winner">Winner: {theme.winner}</span>
          </div>
          <p class="theme-description">{theme.description}</p>
        </div>
      {/each}
    </div>
  </div>

  <!-- Musical Taste Profiles -->
  <div class="section-block">
    <h3>🎵 Musical DNA Analysis</h3>
    <div class="taste-profiles">
      {#each analytics.musicalTaste as profile}
        {@const member = getMemberById(profile.member.toLowerCase())}
        <div class="taste-card card">
          <div class="taste-header">
            <img src={member?.avatar} alt={member?.name} class="taste-avatar" />
            <div>
              <h4>{profile.member}</h4>
              <p class="taste-signature">{profile.signature}</p>
            </div>
          </div>
          <div class="genres-section">
            <strong>Primary Genres:</strong>
            <div class="genres-list">
              {#each profile.primaryGenres as genre}
                <span class="genre-tag">{genre}</span>
              {/each}
            </div>
          </div>
          <div class="influences-section">
            <strong>Key Influences:</strong>
            <div class="influences-list">
              {profile.influences.join(" • ")}
            </div>
          </div>
        </div>
      {/each}
    </div>
  </div>
</section>

<style>
  .analytics-section {
    padding: var(--space-2xl) 0;
  }
  
  .analytics-header {
    text-align: center;
    margin-bottom: var(--space-3xl);
  }
  
  .analytics-header h2 {
    font-size: var(--text-4xl);
    margin-bottom: var(--space-md);
    background: linear-gradient(135deg, var(--color-primary), var(--color-accent));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  
  .analytics-subtitle {
    font-size: var(--text-lg);
    color: var(--color-text-secondary);
    margin-bottom: var(--space-xl);
  }
  
  .overview-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: var(--space-lg);
    max-width: 800px;
    margin: 0 auto;
  }
  
  .overview-stat {
    text-align: center;
    padding: var(--space-lg);
    background: var(--color-bg-secondary);
    border-radius: var(--radius-lg);
    border: 1px solid var(--color-border);
  }
  
  .section-block {
    margin-bottom: var(--space-3xl);
  }
  
  .section-block h3 {
    text-align: center;
    font-size: var(--text-3xl);
    margin-bottom: var(--space-xl);
  }
  
  /* Leaderboard Styles */
  .leaderboard {
    max-width: 1000px;
    margin: 0 auto;
  }
  
  .leaderboard-item {
    display: grid;
    grid-template-columns: auto auto 1fr auto;
    gap: var(--space-lg);
    align-items: center;
    padding: var(--space-lg);
    margin-bottom: var(--space-md);
    background: var(--color-bg-secondary);
    border-radius: var(--radius-lg);
    border: 1px solid var(--color-border);
    transition: transform var(--transition-base);
  }
  
  .leaderboard-item:hover {
    transform: translateY(-2px);
  }
  
  .rank-1 {
    border-left: 4px solid gold;
    background: linear-gradient(135deg, var(--color-bg-secondary), rgba(255, 215, 0, 0.1));
  }
  
  .rank-2 {
    border-left: 4px solid silver;
  }
  
  .rank-3 {
    border-left: 4px solid #cd7f32;
  }
  
  .rank-badge {
    font-size: var(--text-2xl);
    font-weight: 700;
    color: var(--color-primary);
    width: 40px;
    text-align: center;
  }
  
  .player-avatar {
    width: 60px;
    height: 60px;
    border-radius: var(--radius-full);
    object-fit: cover;
    border: 2px solid var(--color-border);
  }
  
  .player-info h4 {
    margin: 0 0 var(--space-xs) 0;
    font-size: var(--text-lg);
  }
  
  .discord-name {
    margin: 0;
    font-size: var(--text-sm);
    color: var(--color-primary);
    font-family: var(--font-mono);
  }
  
  .player-stats {
    text-align: right;
  }
  
  .main-stat {
    margin-bottom: var(--space-sm);
  }
  
  .total-points {
    font-size: var(--text-3xl);
    font-weight: 700;
    color: var(--color-primary);
  }
  
  .points-label {
    font-size: var(--text-sm);
    color: var(--color-text-secondary);
    margin-left: var(--space-xs);
  }
  
  .secondary-stats {
    display: flex;
    gap: var(--space-md);
    justify-content: flex-end;
    margin-bottom: var(--space-sm);
    font-size: var(--text-sm);
  }
  
  .best-song {
    font-size: var(--text-sm);
    color: var(--color-text-secondary);
    max-width: 300px;
  }
  
  /* Voting Grid */
  .voting-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: var(--space-lg);
  }
  
  .voting-card .voter-header {
    display: flex;
    align-items: center;
    gap: var(--space-md);
    margin-bottom: var(--space-lg);
  }
  
  .voter-avatar {
    width: 50px;
    height: 50px;
    border-radius: var(--radius-full);
    object-fit: cover;
  }
  
  .voting-style {
    color: var(--color-accent);
    font-weight: 600;
    margin: 0;
  }
  
  .voting-stats {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--space-md);
    margin-bottom: var(--space-lg);
    text-align: center;
  }
  
  .voting-stat .stat-value {
    display: block;
    font-size: var(--text-xl);
    font-weight: 700;
    color: var(--color-primary);
  }
  
  .voting-patterns .pattern-item {
    display: flex;
    justify-content: space-between;
    margin-bottom: var(--space-sm);
    font-size: var(--text-sm);
  }
  
  /* Controversy List */
  .controversy-list {
    max-width: 800px;
    margin: 0 auto;
  }
  
  .controversy-item {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: var(--space-lg);
    align-items: center;
    margin-bottom: var(--space-md);
  }
  
  .song-title {
    margin: 0 0 var(--space-xs) 0;
    color: var(--color-primary);
  }
  
  .song-artist, .song-submitter {
    margin: 0;
    font-size: var(--text-sm);
    color: var(--color-text-secondary);
  }
  
  .controversy-stats {
    display: flex;
    gap: var(--space-lg);
    text-align: center;
  }
  
  .variance-score, .score-value {
    display: block;
    font-size: var(--text-xl);
    font-weight: 700;
    color: var(--color-error);
  }
  
  .controversy-reason {
    grid-column: 1 / -1;
    margin-top: var(--space-md);
    color: var(--color-text-secondary);
  }
  
  /* Streaks */
  .streaks-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: var(--space-lg);
  }
  
  .streak-title {
    margin-bottom: var(--space-md);
  }
  
  .streak-member {
    font-size: var(--text-lg);
    font-weight: 700;
    color: var(--color-primary);
  }
  
  .streak-type {
    font-size: var(--text-md);
    color: var(--color-accent);
    font-weight: 600;
    margin-left: var(--space-sm);
  }
  
  /* Theme Analysis */
  .themes-list {
    max-width: 800px;
    margin: 0 auto;
  }
  
  .theme-item {
    padding: var(--space-lg);
    margin-bottom: var(--space-md);
    background: var(--color-bg-secondary);
    border-radius: var(--radius-lg);
    border: 1px solid var(--color-border);
  }
  
  .theme-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: var(--space-md);
  }
  
  .difficulty-badge {
    padding: var(--space-xs) var(--space-sm);
    border-radius: var(--radius-sm);
    font-size: var(--text-xs);
    font-weight: 700;
    text-transform: uppercase;
  }
  
  .difficulty-meta { background: var(--color-accent); color: white; }
  .difficulty-medium { background: var(--color-warning); color: white; }
  .difficulty-hard { background: var(--color-error); color: white; }
  .difficulty-expert { background: #8b5cf6; color: white; }
  
  /* Musical Taste */
  .taste-profiles {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: var(--space-lg);
  }
  
  .taste-header {
    display: flex;
    align-items: center;
    gap: var(--space-md);
    margin-bottom: var(--space-lg);
  }
  
  .taste-avatar {
    width: 50px;
    height: 50px;
    border-radius: var(--radius-full);
    object-fit: cover;
  }
  
  .taste-signature {
    color: var(--color-accent);
    font-style: italic;
    margin: 0;
  }
  
  .genres-list {
    display: flex;
    flex-wrap: wrap;
    gap: var(--space-xs);
    margin: var(--space-sm) 0 var(--space-md) 0;
  }
  
  .genre-tag {
    padding: var(--space-xs) var(--space-sm);
    background: var(--color-primary);
    color: white;
    border-radius: var(--radius-sm);
    font-size: var(--text-xs);
    font-weight: 600;
  }
  
  .influences-list {
    color: var(--color-text-secondary);
    font-size: var(--text-sm);
    margin-top: var(--space-sm);
  }
  
  /* Color utilities */
  .text-green-500 { color: #10b981; }
  .text-yellow-500 { color: #f59e0b; }
  .text-orange-500 { color: #f97316; }
  .text-red-500 { color: #ef4444; }
  
  @media (max-width: 768px) {
    .overview-stats {
      grid-template-columns: repeat(2, 1fr);
    }
    
    .leaderboard-item {
      grid-template-columns: auto 1fr;
      gap: var(--space-md);
    }
    
    .rank-badge {
      grid-row: 1 / 3;
    }
    
    .player-stats {
      grid-column: 1 / -1;
      text-align: left;
      margin-top: var(--space-md);
    }
    
    .secondary-stats {
      justify-content: flex-start;
    }
    
    .controversy-item {
      grid-template-columns: 1fr;
    }
    
    .controversy-stats {
      justify-content: space-around;
    }
  }
</style>