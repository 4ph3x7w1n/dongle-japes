<script lang="ts">
  import { onMount } from 'svelte';
  import Navigation from '$lib/components/Navigation.svelte';
  import MemberCard from '$lib/components/MemberCard.svelte';
  import RecordClub from '$lib/components/RecordClub.svelte';
  import MusicLeagueAnalytics from '$lib/components/MusicLeagueAnalytics.svelte';
  import { theme } from '$lib/stores/theme';
  import { members } from '$lib/data/members';
  import { loreEntries } from '$lib/data/lore';
  import { musicLeagueRounds } from '$lib/data/musicLeague';
  import { events } from '$lib/data/events';
  import { discordStats } from '$lib/data/discord';
  
  onMount(() => {
    theme.init();
  });
</script>

<Navigation />

<main>
  <!-- Hero Section -->
  <section id="home" class="hero section">
    <div class="container hero-content">
      <div class="hero-text animate-fadeIn">
        <h1 class="hero-title">
          <span class="gradient-text">The Dongle Japes</span>
        </h1>
        <p class="hero-subtitle">
          High school friends who discovered that distance means nothing when you have Discord, shared playlists, and an endless supply of inside jokes.
        </p>
        <p class="hero-motto">
          "We came for the dongles, we stayed for the japes."
        </p>
        <div class="hero-actions">
          <a href="#about" class="button">Meet the Crew</a>
          <a href="https://discord.com/channels/817843318880862298/817843318880862300" target="_blank" class="button button-secondary">Discord</a>
        </div>
      </div>
      
      <div class="hero-visual animate-fadeIn">
        <div class="social-links">
          <h3>Connect With Us</h3>
          <div class="links-grid">
            <a href="https://discord.com/channels/817843318880862298/817843318880862300" target="_blank" class="social-link card">
              <div class="social-icon">💬</div>
              <div class="social-info">
                <h4>Discord</h4>
                <p>Our digital headquarters</p>
              </div>
            </a>
            
            <a href="https://groupme.com/join_group/14807452/08SYus" target="_blank" class="social-link card">
              <div class="social-icon">📱</div>
              <div class="social-info">
                <h4>GroupMe</h4>
                <p>Quick chats on the go</p>
              </div>
            </a>
            
            <a href="https://docs.google.com/spreadsheets/d/1fH_nLo9NMX9f5e0pnZe1rX0jhAHK4Ex-CnA9ZCkQ3RM/edit?gid=0#gid=0" target="_blank" class="social-link card">
              <div class="social-icon">📊</div>
              <div class="social-info">
                <h4>Record Club Sheets</h4>
                <p>Album reviews & ratings</p>
              </div>
            </a>
            
            <a href="https://app.musicleague.com/l/04c6de304dd741b898832561a62a18e4/" target="_blank" class="social-link card">
              <div class="social-icon">🎵</div>
              <div class="social-info">
                <h4>Music League</h4>
                <p>Musical battlegrounds</p>
              </div>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- About Section -->
  <section id="about" class="section">
    <div class="container">
      <h2 class="section-title">Meet The Dongle Japes</h2>
      <p class="section-subtitle">
        A legendary crew of friends who turned a Discord server into a digital home
      </p>
      
      <div class="members-grid">
        {#each members as member}
          <MemberCard {member} />
        {/each}
      </div>
      
      <div class="origin-story card">
        <h3>Our Origin Story</h3>
        <p>
          A tight-knit group of friends from high school who discovered that graduation doesn't have to mean goodbye. 
          When life scattered us across different cities and colleges, we found our home base in 
          Discord—where distance became irrelevant and friendships grew stronger through shared 
          playlists, endless memes, and 3 AM philosophical debates about dongles.
        </p>
        <p>
          Since March 2020, The Dongle Japes have been setting the gold standard for long-distance 
          friendship. From intense Music League competitions that reveal questionable taste to 
          Record Club sessions that spark passionate album debates, we've proven that the best 
          bonds are built on inside jokes, musical discovery, and an unhealthy obsession with tacos.
        </p>
      </div>
    </div>
  </section>

  <!-- Lore Section -->
  <section id="lore" class="section bg-secondary">
    <div class="container">
      <h2 class="section-title">The Sacred Lore</h2>
      <p class="section-subtitle">
        Chronicles of chaos, wisdom, and legendary moments
      </p>
      
      <div class="lore-timeline">
        {#each loreEntries as entry}
          <div class="lore-entry card">
            <div class="lore-date">{new Date(entry.date).toLocaleDateString()}</div>
            <div class="lore-type">{entry.type}</div>
            <h4 class="lore-title">{entry.title}</h4>
            <p class="lore-description">{entry.description}</p>
            <div class="lore-members">
              {#each entry.involvedMembers as memberId}
                {@const member = members.find(m => m.id === memberId)}
                {#if member}
                  <span class="lore-member">{member.discordName}</span>
                {/if}
              {/each}
            </div>
          </div>
        {/each}
      </div>
    </div>
  </section>

  <!-- Music League Analytics Section -->
  <section id="music" class="section">
    <div class="container">
      <MusicLeagueAnalytics />
    </div>
  </section>
  
  <!-- Record Club Section -->
  <section id="records" class="section bg-secondary">
    <div class="container">
      <RecordClub />
    </div>
  </section>

  <!-- Events Section -->
  <section id="events" class="section bg-secondary">
    <div class="container">
      <h2 class="section-title">Events & Hangouts</h2>
      <p class="section-subtitle">
        Where friendship meets coordinated chaos
      </p>
      
      <div class="events-grid">
        {#each events as event}
          <div class="event-card card">
            <div class="event-type">{event.type}</div>
            <h4>{event.title}</h4>
            <div class="event-date">{new Date(event.date).toLocaleDateString()}</div>
            <p>{event.description}</p>
            {#if event.location}
              <div class="event-location">📍 {event.location}</div>
            {/if}
            <div class="event-attendees">
              {#each event.attendees as attendeeId}
                {@const member = members.find(m => m.id === attendeeId)}
                {#if member}
                  <span class="attendee">{member.discordName}</span>
                {/if}
              {/each}
            </div>
          </div>
        {/each}
      </div>
    </div>
  </section>

  <!-- Birthdays Section -->
  <section id="birthdays" class="section">
    <div class="container">
      <h2 class="section-title">Birthday Calendar</h2>
      <p class="section-subtitle">
        Annual celebrations of existence and cake consumption
      </p>
      
      <div class="birthday-grid">
        {#each members as member}
          <div class="birthday-card card">
            <div class="birthday-month">
              {new Date(member.birthday).toLocaleDateString('en-US', { month: 'long' })}
            </div>
            <div class="birthday-day">
              {new Date(member.birthday).getDate()}
            </div>
            <div class="birthday-info">
              <h4>{member.name}</h4>
              <p>@{member.discordName}</p>
            </div>
            <div class="birthday-cake">🎂</div>
          </div>
        {/each}
      </div>
    </div>
  </section>

  <!-- Discord Section -->
  <section id="discord" class="section bg-secondary">
    <div class="container">
      <h2 class="section-title">Discord Command Center</h2>
      <p class="section-subtitle">
        Our digital headquarters and meme repository
      </p>
      
      <div class="discord-stats">
        <div class="stat-card card">
          <h3>Server Stats</h3>
          <div class="stats-grid">
            <div class="stat">
              <span class="stat-number">{discordStats.totalMessages.toLocaleString()}</span>
              <span class="stat-label">Total Messages</span>
            </div>
            <div class="stat">
              <span class="stat-number">{discordStats.voiceHours}</span>
              <span class="stat-label">Voice Hours</span>
            </div>
            <div class="stat">
              <span class="stat-number">{discordStats.memberCount}</span>
              <span class="stat-label">Elite Members</span>
            </div>
          </div>
        </div>
        
        <div class="emoji-stats card">
          <h3>Top Emojis</h3>
          <div class="emoji-list">
            {#each discordStats.topEmojis.slice(0, 6) as emoji}
              <div class="emoji-stat">
                <span class="emoji">{emoji.emoji}</span>
                <span class="emoji-count">{emoji.count}</span>
              </div>
            {/each}
          </div>
        </div>
        
        <div class="channels-stats card">
          <h3>Top Channels</h3>
          <div class="channels-list">
            {#each discordStats.topChannels.slice(0, 4) as channel}
              <div class="channel-stat">
                <span class="channel-name">#{channel.name}</span>
                <span class="channel-count">{channel.messageCount.toLocaleString()}</span>
              </div>
            {/each}
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- Gallery Section -->
  <section id="gallery" class="section">
    <div class="container">
      <h2 class="section-title">Gallery of Memories</h2>
      <p class="section-subtitle">
        Screenshots, memes, and moments worth preserving
      </p>
      
      <div class="gallery-placeholder card">
        <div class="placeholder-content">
          <h3>🖼️ Gallery Coming Soon</h3>
          <p>This is where all the legendary screenshots, memes, and group photos will live. 
             Upload your favorite Dongle Japes moments here!</p>
          <button class="button">Upload Memories</button>
        </div>
      </div>
    </div>
  </section>

  <!-- Contact Section -->
  <section id="contact" class="section bg-secondary">
    <div class="container">
      <h2 class="section-title">Join The Japes</h2>
      <p class="section-subtitle">
        Think you have what it takes to be a Dongle Jape?
      </p>
      
      <div class="contact-content">
        <div class="join-requirements card">
          <h3>Membership Requirements</h3>
          <ul>
            <li>Must appreciate quality memes</li>
            <li>Willing to participate in 3 AM philosophical discussions</li>
            <li>Can tolerate Chris saying "bruh" 47 times per day</li>
            <li>Enjoys tacos (non-negotiable)</li>
            <li>Ready to lose at Music League spectacularly</li>
          </ul>
        </div>
        
        <div class="contact-form card">
          <h3>Honorary Membership Application</h3>
          <form>
            <input type="text" placeholder="Your Name" required />
            <input type="text" placeholder="Discord Username" required />
            <textarea placeholder="Why do you want to join The Dongle Japes?" required></textarea>
            <button type="submit" class="button">Submit Application</button>
          </form>
        </div>
      </div>
    </div>
  </section>
</main>

<!-- Footer -->
<footer class="footer">
  <div class="container">
    <div class="footer-content">
      <div class="footer-section">
        <h4>The Dongle Japes</h4>
        <p>Est. March 2020</p>
        <p>"We came for the dongles, we stayed for the japes."</p>
      </div>
      
      <div class="footer-section">
        <h4>Quick Links</h4>
        <ul>
          <li><a href="#about">About</a></li>
          <li><a href="#lore">Lore</a></li>
          <li><a href="#music">Music League</a></li>
          <li><a href="#records">Record Club</a></li>
          <li><a href="#discord">Discord</a></li>
        </ul>
      </div>
      
      <div class="footer-section">
        <h4>Connect</h4>
        <p>Discord: [INVITE_LINK_HERE]</p>
        <p>Spotify: [PLAYLIST_LINK_HERE]</p>
      </div>
    </div>
    
    <div class="footer-bottom">
      <p>&copy; 2024 The Dongle Japes. All memes reserved.</p>
      <p><small>Disclaimer: No actual dongles were harmed in the making of this friendship.</small></p>
    </div>
  </div>
</footer>

<style>
  /* Hero Section */
  .hero {
    min-height: 100vh;
    display: flex;
    align-items: center;
    background: linear-gradient(135deg, var(--color-bg) 0%, var(--color-bg-secondary) 100%);
    position: relative;
    overflow: hidden;
  }
  
  .hero::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url("data:image/svg+xml,%3Csvg width='60' height='60' viewBox='0 0 60 60' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23646cff' fill-opacity='0.03'%3E%3Ccircle cx='30' cy='30' r='4'/%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
    pointer-events: none;
  }
  
  .hero-content {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--space-3xl);
    align-items: center;
    position: relative;
    z-index: 1;
  }
  
  .hero-title {
    font-size: clamp(var(--text-4xl), 8vw, var(--text-5xl));
    margin-bottom: var(--space-lg);
    line-height: 1.1;
  }
  
  .gradient-text {
    background: linear-gradient(135deg, var(--color-primary), var(--color-accent));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  
  .hero-subtitle {
    font-size: var(--text-xl);
    color: var(--color-text-secondary);
    margin-bottom: var(--space-lg);
    line-height: 1.5;
  }
  
  .hero-motto {
    font-size: var(--text-lg);
    font-style: italic;
    color: var(--color-accent);
    margin-bottom: var(--space-2xl);
    padding: var(--space-md);
    border-left: 4px solid var(--color-accent);
    background: var(--color-bg-secondary);
    border-radius: var(--radius-md);
  }
  
  .hero-actions {
    display: flex;
    gap: var(--space-md);
    flex-wrap: wrap;
  }
  
  .button-secondary {
    background: transparent;
    color: var(--color-primary);
    border: 2px solid var(--color-primary);
  }
  
  .button-secondary:hover {
    background: var(--color-primary);
    color: white;
  }
  
  
  .social-links {
    text-align: center;
  }
  
  .social-links h3 {
    margin-bottom: var(--space-xl);
    color: var(--color-text);
  }
  
  .links-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: var(--space-lg);
  }
  
  .social-link {
    display: flex;
    align-items: center;
    gap: var(--space-md);
    text-decoration: none;
    transition: transform var(--transition-base), background var(--transition-base);
    padding: var(--space-lg);
  }
  
  .social-link:hover {
    transform: translateY(-4px);
    background: var(--color-bg-tertiary);
  }
  
  .social-icon {
    font-size: var(--text-3xl);
    flex-shrink: 0;
  }
  
  .social-info {
    text-align: left;
  }
  
  .social-info h4 {
    margin: 0 0 var(--space-xs) 0;
    color: var(--color-primary);
    font-size: var(--text-lg);
  }
  
  .social-info p {
    margin: 0;
    color: var(--color-text-secondary);
    font-size: var(--text-sm);
  }
  
  /* Sections */
  .section-title {
    text-align: center;
    margin-bottom: var(--space-md);
  }
  
  .section-subtitle {
    text-align: center;
    color: var(--color-text-secondary);
    margin-bottom: var(--space-2xl);
    font-size: var(--text-lg);
  }
  
  .bg-secondary {
    background: var(--color-bg-secondary);
  }
  
  /* Members Grid */
  .members-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: var(--space-xl);
    margin-bottom: var(--space-2xl);
  }
  
  .origin-story {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
  }
  
  /* Lore Timeline */
  .lore-timeline {
    display: grid;
    gap: var(--space-lg);
    max-width: 800px;
    margin: 0 auto;
  }
  
  .lore-entry {
    position: relative;
    padding-left: var(--space-3xl);
  }
  
  .lore-entry::before {
    content: '';
    position: absolute;
    left: var(--space-md);
    top: var(--space-md);
    width: 12px;
    height: 12px;
    background: var(--color-primary);
    border-radius: var(--radius-full);
  }
  
  .lore-entry::after {
    content: '';
    position: absolute;
    left: calc(var(--space-md) + 5px);
    top: calc(var(--space-md) + 12px);
    width: 2px;
    height: calc(100% - var(--space-md));
    background: var(--color-border);
  }
  
  .lore-entry:last-child::after {
    display: none;
  }
  
  .lore-date {
    font-size: var(--text-sm);
    color: var(--color-text-tertiary);
  }
  
  .lore-type {
    display: inline-block;
    padding: var(--space-xs) var(--space-sm);
    background: var(--color-primary);
    color: white;
    border-radius: var(--radius-sm);
    font-size: var(--text-xs);
    text-transform: uppercase;
    font-weight: 600;
    margin: var(--space-xs) 0;
  }
  
  .lore-title {
    margin-bottom: var(--space-sm);
  }
  
  .lore-members {
    display: flex;
    gap: var(--space-sm);
    margin-top: var(--space-md);
    flex-wrap: wrap;
  }
  
  .lore-member {
    padding: var(--space-xs) var(--space-sm);
    background: var(--color-bg-tertiary);
    border-radius: var(--radius-sm);
    font-size: var(--text-sm);
    color: var(--color-text-secondary);
  }
  
  
  /* Events */
  .events-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: var(--space-lg);
  }
  
  .event-type {
    display: inline-block;
    padding: var(--space-xs) var(--space-sm);
    background: var(--color-accent);
    color: white;
    border-radius: var(--radius-sm);
    font-size: var(--text-xs);
    text-transform: uppercase;
    font-weight: 600;
    margin-bottom: var(--space-sm);
  }
  
  .event-attendees {
    display: flex;
    gap: var(--space-xs);
    margin-top: var(--space-md);
    flex-wrap: wrap;
  }
  
  .attendee {
    padding: var(--space-xs) var(--space-sm);
    background: var(--color-bg-tertiary);
    border-radius: var(--radius-sm);
    font-size: var(--text-sm);
  }
  
  /* Birthdays */
  .birthday-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: var(--space-lg);
  }
  
  .birthday-card {
    display: grid;
    grid-template-columns: auto 1fr auto;
    align-items: center;
    gap: var(--space-md);
  }
  
  .birthday-month {
    font-size: var(--text-sm);
    color: var(--color-text-secondary);
    text-transform: uppercase;
    font-weight: 600;
  }
  
  .birthday-day {
    font-size: var(--text-3xl);
    font-weight: 700;
    color: var(--color-primary);
  }
  
  .birthday-cake {
    font-size: var(--text-2xl);
  }
  
  /* Discord Stats */
  .discord-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: var(--space-lg);
  }
  
  .stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(100px, 1fr));
    gap: var(--space-md);
    text-align: center;
  }
  
  .emoji-list,
  .channels-list {
    display: grid;
    gap: var(--space-sm);
  }
  
  .emoji-stat,
  .channel-stat {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: var(--space-sm);
    background: var(--color-bg-tertiary);
    border-radius: var(--radius-md);
  }
  
  .emoji {
    font-size: var(--text-lg);
  }
  
  /* Gallery */
  .gallery-placeholder {
    text-align: center;
    padding: var(--space-3xl);
  }
  
  /* Contact */
  .contact-content {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: var(--space-xl);
    max-width: 1000px;
    margin: 0 auto;
  }
  
  .join-requirements ul {
    list-style: none;
    padding: 0;
  }
  
  .join-requirements li {
    padding: var(--space-sm) 0;
    border-bottom: 1px solid var(--color-border);
  }
  
  .join-requirements li::before {
    content: '✓';
    color: var(--color-success);
    font-weight: bold;
    margin-right: var(--space-sm);
  }
  
  .contact-form form {
    display: grid;
    gap: var(--space-md);
  }
  
  .contact-form input,
  .contact-form textarea {
    padding: var(--space-md);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    background: var(--color-bg);
    color: var(--color-text);
    font-family: inherit;
  }
  
  .contact-form textarea {
    resize: vertical;
    min-height: 120px;
  }
  
  /* Footer */
  .footer {
    background: var(--color-bg-tertiary);
    border-top: 1px solid var(--color-border);
    padding: var(--space-2xl) 0 var(--space-lg);
  }
  
  .footer-content {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: var(--space-xl);
    margin-bottom: var(--space-xl);
  }
  
  .footer-section h4 {
    margin-bottom: var(--space-md);
    color: var(--color-text);
  }
  
  .footer-section ul {
    list-style: none;
    padding: 0;
  }
  
  .footer-section li {
    margin-bottom: var(--space-sm);
  }
  
  .footer-bottom {
    text-align: center;
    padding-top: var(--space-lg);
    border-top: 1px solid var(--color-border);
    color: var(--color-text-secondary);
  }
  
  /* Mobile Responsive */
  @media (max-width: 768px) {
    .hero-content {
      grid-template-columns: 1fr;
      text-align: center;
    }
    
    .links-grid {
      grid-template-columns: 1fr;
    }
    
    .social-link {
      justify-content: center;
      text-align: center;
    }
    
    .social-info {
      text-align: center;
    }
    
    .contact-content {
      grid-template-columns: 1fr;
    }
    
    .hero-actions {
      justify-content: center;
    }
  }
</style>