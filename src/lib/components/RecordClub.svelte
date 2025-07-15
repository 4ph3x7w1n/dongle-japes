<script lang="ts">
  import { members } from '$lib/data/members';
  
  // Record Club Data - replace with real data from Rekkert Bois.xlsx when available
  const recordClubData = {
    name: "Rekkert Bois Record Club",
    totalAlbums: 47,
    avgRating: 7.2,
    mostActiveReviewer: "Dylan",
    recentAlbums: [
      {
        id: 1,
        title: "Harvest Moon",
        artist: "Neil Young",
        reviewer: "Max",
        rating: 9.2,
        date: "2024-12-15",
        reviewSnippet: "Wire to wire perfection. Neil Young is the foundation of everything good in music.",
        favoriteTrack: "Harvest Moon",
        tags: ["Folk", "Classic Rock"]
      },
      {
        id: 2,
        title: "Z",
        artist: "My Morning Jacket",
        reviewer: "Dylan",
        rating: 8.8,
        date: "2024-12-08",
        reviewSnippet: "MMJ in their prime. Laylow alone makes this album essential listening for any guitar enthusiast.",
        favoriteTrack: "Laylow",
        tags: ["Indie Rock", "Southern Rock"]
      },
      {
        id: 3,
        title: "Cosmogramma",
        artist: "Flying Lotus",
        reviewer: "Chris",
        rating: 7.5,
        date: "2024-12-01",
        reviewSnippet: "Experimental jazz-electronic fusion that challenges conventional music boundaries.",
        favoriteTrack: "...And The World Laughs With You",
        tags: ["Electronic", "Jazz Fusion"]
      },
      {
        id: 4,
        title: "Make It Big",
        artist: "Wham!",
        reviewer: "Adam",
        rating: 6.9,
        date: "2024-11-24",
        reviewSnippet: "Peak 80s energy. George Michael's voice carries the entire project.",
        favoriteTrack: "Careless Whisper",
        tags: ["Pop", "80s"]
      }
    ],
    memberStats: [
      {
        memberId: "dylan",
        albumsReviewed: 14,
        avgRating: 7.8,
        wordCount: 8947,
        favoriteGenres: ["Indie Rock", "Jam Band", "Folk"],
        signature: "Novel-length philosophical reviews"
      },
      {
        memberId: "max",
        albumsReviewed: 12,
        avgRating: 7.1,
        wordCount: 3421,
        favoriteGenres: ["Folk", "Indie", "Alternative"],
        signature: "Neil Young references guaranteed"
      },
      {
        memberId: "chris",
        albumsReviewed: 11,
        avgRating: 6.8,
        wordCount: 2156,
        favoriteGenres: ["Electronic", "World", "Experimental"],
        signature: "Wildcard international picks"
      },
      {
        memberId: "adam",
        albumsReviewed: 10,
        avgRating: 7.4,
        wordCount: 1987,
        favoriteGenres: ["Classic Rock", "Pop", "Soul"],
        signature: "Nostalgic deep cuts"
      }
    ],
    rules: [
      "One album per week, rotating reviewers",
      "Reviews must be at least 200 words",
      "Include favorite track and rating out of 10",
      "Group discussion required within 48 hours",
      "No albums from current year (let them age)",
      "Dylan's reviews cannot exceed 2000 words (frequently ignored)"
    ]
  };
  
  function getMemberById(id: string) {
    return members.find(m => m.id === id);
  }
  
  function getScoreColor(rating: number) {
    if (rating >= 8.5) return 'text-green-500';
    if (rating >= 7.0) return 'text-yellow-500';
    if (rating >= 5.5) return 'text-orange-500';
    return 'text-red-500';
  }
</script>

<section class="record-club-section">
  <div class="club-header">
    <h2>🎵 {recordClubData.name}</h2>
    <p class="club-subtitle">Where musical taste goes to die... gloriously</p>
    
    <div class="club-stats">
      <div class="stat-item">
        <span class="stat-number">{recordClubData.totalAlbums}</span>
        <span class="stat-label">Albums Reviewed</span>
      </div>
      <div class="stat-item">
        <span class="stat-number">{recordClubData.avgRating}/10</span>
        <span class="stat-label">Average Rating</span>
      </div>
      <div class="stat-item">
        <span class="stat-number">{recordClubData.mostActiveReviewer}</span>
        <span class="stat-label">Most Active Reviewer</span>
      </div>
    </div>
  </div>

  <div class="recent-reviews">
    <h3>Recent Reviews</h3>
    <div class="reviews-grid">
      {#each recordClubData.recentAlbums as album}
        {@const reviewer = getMemberById(album.reviewer.toLowerCase())}
        <div class="review-card card">
          <div class="album-header">
            <div class="album-info">
              <h4 class="album-title">{album.title}</h4>
              <p class="album-artist">{album.artist}</p>
              <div class="album-meta">
                <span class="reviewer">Reviewed by {reviewer?.discordName || album.reviewer}</span>
                <span class="review-date">{new Date(album.date).toLocaleDateString()}</span>
              </div>
            </div>
            <div class="album-rating">
              <span class="rating-score {getScoreColor(album.rating)}">{album.rating}</span>
              <span class="rating-scale">/10</span>
            </div>
          </div>
          
          <div class="album-tags">
            {#each album.tags as tag}
              <span class="tag">{tag}</span>
            {/each}
          </div>
          
          <blockquote class="review-snippet">
            "{album.reviewSnippet}"
          </blockquote>
          
          <div class="favorite-track">
            <span class="track-label">🎧 Standout Track:</span>
            <span class="track-name">{album.favoriteTrack}</span>
          </div>
        </div>
      {/each}
    </div>
  </div>

  <div class="member-breakdown">
    <h3>Reviewer Statistics</h3>
    <div class="members-stats">
      {#each recordClubData.memberStats as memberStat}
        {@const member = getMemberById(memberStat.memberId)}
        <div class="member-stat-card card">
          <div class="member-header">
            <img 
              src={member?.avatar || '/pics/placeholder.png'} 
              alt={member?.name}
              class="member-avatar-small"
            />
            <div class="member-info">
              <h4>{member?.name}</h4>
              <p class="member-discord">@{member?.discordName}</p>
            </div>
          </div>
          
          <div class="stat-grid">
            <div class="stat">
              <span class="stat-value">{memberStat.albumsReviewed}</span>
              <span class="stat-desc">Albums</span>
            </div>
            <div class="stat">
              <span class="stat-value {getScoreColor(memberStat.avgRating)}">{memberStat.avgRating}</span>
              <span class="stat-desc">Avg Rating</span>
            </div>
            <div class="stat">
              <span class="stat-value">{memberStat.wordCount.toLocaleString()}</span>
              <span class="stat-desc">Words Written</span>
            </div>
          </div>
          
          <div class="member-signature">
            <strong>Signature Style:</strong> {memberStat.signature}
          </div>
          
          <div class="favorite-genres">
            <strong>Go-to Genres:</strong>
            {#each memberStat.favoriteGenres as genre, i}
              <span class="genre">{genre}</span>{#if i < memberStat.favoriteGenres.length - 1}, {/if}
            {/each}
          </div>
        </div>
      {/each}
    </div>
  </div>

  <div class="club-rules">
    <h3>Record Club Constitution</h3>
    <div class="rules-card card">
      <ul class="rules-list">
        {#each recordClubData.rules as rule}
          <li class="rule-item">{rule}</li>
        {/each}
      </ul>
    </div>
  </div>
</section>

<style>
  .record-club-section {
    padding: var(--space-2xl) 0;
  }
  
  .club-header {
    text-align: center;
    margin-bottom: var(--space-2xl);
  }
  
  .club-header h2 {
    font-size: var(--text-4xl);
    margin-bottom: var(--space-md);
    background: linear-gradient(135deg, var(--color-primary), var(--color-accent));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  
  .club-subtitle {
    font-size: var(--text-lg);
    color: var(--color-text-secondary);
    margin-bottom: var(--space-xl);
  }
  
  .club-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: var(--space-lg);
    max-width: 600px;
    margin: 0 auto;
  }
  
  .stat-item {
    text-align: center;
    padding: var(--space-md);
    background: var(--color-bg-secondary);
    border-radius: var(--radius-lg);
    border: 1px solid var(--color-border);
  }
  
  .stat-number {
    display: block;
    font-size: var(--text-2xl);
    font-weight: 700;
    color: var(--color-primary);
  }
  
  .stat-label {
    font-size: var(--text-sm);
    color: var(--color-text-secondary);
  }
  
  .recent-reviews {
    margin-bottom: var(--space-2xl);
  }
  
  .recent-reviews h3 {
    text-align: center;
    margin-bottom: var(--space-xl);
    font-size: var(--text-3xl);
  }
  
  .reviews-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: var(--space-lg);
  }
  
  .review-card {
    transition: transform var(--transition-base);
  }
  
  .review-card:hover {
    transform: translateY(-4px);
  }
  
  .album-header {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    margin-bottom: var(--space-md);
  }
  
  .album-title {
    font-size: var(--text-xl);
    font-weight: 700;
    margin: 0 0 var(--space-xs) 0;
    color: var(--color-text);
  }
  
  .album-artist {
    font-size: var(--text-lg);
    color: var(--color-text-secondary);
    margin: 0 0 var(--space-sm) 0;
  }
  
  .album-meta {
    display: flex;
    flex-direction: column;
    gap: var(--space-xs);
    font-size: var(--text-sm);
    color: var(--color-text-tertiary);
  }
  
  .album-rating {
    text-align: right;
    flex-shrink: 0;
  }
  
  .rating-score {
    font-size: var(--text-3xl);
    font-weight: 700;
  }
  
  .rating-scale {
    font-size: var(--text-lg);
    color: var(--color-text-tertiary);
  }
  
  .album-tags {
    display: flex;
    flex-wrap: wrap;
    gap: var(--space-xs);
    margin-bottom: var(--space-md);
  }
  
  .tag {
    padding: var(--space-xs) var(--space-sm);
    background: var(--color-primary);
    color: white;
    border-radius: var(--radius-sm);
    font-size: var(--text-xs);
    font-weight: 600;
  }
  
  .review-snippet {
    font-style: italic;
    margin: var(--space-md) 0;
    padding: var(--space-md);
    border-left: 4px solid var(--color-accent);
    background: var(--color-bg-tertiary);
    border-radius: var(--radius-md);
  }
  
  .favorite-track {
    display: flex;
    align-items: center;
    gap: var(--space-sm);
    padding: var(--space-sm);
    background: var(--color-bg-secondary);
    border-radius: var(--radius-md);
    font-size: var(--text-sm);
  }
  
  .track-label {
    color: var(--color-text-secondary);
  }
  
  .track-name {
    font-weight: 600;
    color: var(--color-primary);
  }
  
  .member-breakdown {
    margin-bottom: var(--space-2xl);
  }
  
  .member-breakdown h3 {
    text-align: center;
    margin-bottom: var(--space-xl);
    font-size: var(--text-3xl);
  }
  
  .members-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: var(--space-lg);
  }
  
  .member-stat-card {
    transition: transform var(--transition-base);
  }
  
  .member-stat-card:hover {
    transform: translateY(-2px);
  }
  
  .member-header {
    display: flex;
    align-items: center;
    gap: var(--space-md);
    margin-bottom: var(--space-lg);
  }
  
  .member-avatar-small {
    width: 50px;
    height: 50px;
    border-radius: var(--radius-full);
    object-fit: cover;
    border: 2px solid var(--color-border);
  }
  
  .member-info h4 {
    margin: 0;
    font-size: var(--text-lg);
  }
  
  .member-discord {
    margin: 0;
    font-size: var(--text-sm);
    color: var(--color-primary);
    font-family: var(--font-mono);
  }
  
  .stat-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--space-md);
    margin-bottom: var(--space-lg);
    text-align: center;
  }
  
  .stat-value {
    display: block;
    font-size: var(--text-xl);
    font-weight: 700;
  }
  
  .stat-desc {
    font-size: var(--text-xs);
    color: var(--color-text-secondary);
    text-transform: uppercase;
    font-weight: 600;
  }
  
  .member-signature {
    margin-bottom: var(--space-md);
    padding: var(--space-sm);
    background: var(--color-bg-tertiary);
    border-radius: var(--radius-md);
    font-size: var(--text-sm);
  }
  
  .favorite-genres {
    font-size: var(--text-sm);
    color: var(--color-text-secondary);
  }
  
  .genre {
    color: var(--color-accent);
    font-weight: 500;
  }
  
  .club-rules h3 {
    text-align: center;
    margin-bottom: var(--space-xl);
    font-size: var(--text-3xl);
  }
  
  .rules-card {
    max-width: 800px;
    margin: 0 auto;
  }
  
  .rules-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .rule-item {
    padding: var(--space-md);
    margin-bottom: var(--space-sm);
    background: var(--color-bg-tertiary);
    border-radius: var(--radius-md);
    border-left: 4px solid var(--color-primary);
    position: relative;
  }
  
  .rule-item::before {
    content: '📝';
    position: absolute;
    left: var(--space-sm);
    top: 50%;
    transform: translateY(-50%);
  }
  
  .rule-item {
    padding-left: calc(var(--space-md) + 24px);
  }
  
  /* Color utilities */
  .text-green-500 { color: #10b981; }
  .text-yellow-500 { color: #f59e0b; }
  .text-orange-500 { color: #f97316; }
  .text-red-500 { color: #ef4444; }
  
  @media (max-width: 768px) {
    .club-stats {
      grid-template-columns: 1fr;
    }
    
    .reviews-grid {
      grid-template-columns: 1fr;
    }
    
    .members-stats {
      grid-template-columns: 1fr;
    }
    
    .album-header {
      flex-direction: column;
      gap: var(--space-md);
    }
    
    .album-rating {
      text-align: left;
    }
  }
</style>