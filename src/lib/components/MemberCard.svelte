<script lang="ts">
  import type { Member } from '$lib/types';
  
  interface Props {
    member: Member;
  }
  
  let { member }: Props = $props();
  
  let showQuotes = $state(false);
  let showAchievements = $state(false);
  
  function toggleQuotes() {
    showQuotes = !showQuotes;
  }
  
  function toggleAchievements() {
    showAchievements = !showAchievements;
  }
  
  function formatDate(dateString: string) {
    return new Date(dateString).toLocaleDateString('en-US', {
      month: 'long',
      day: 'numeric'
    });
  }
</script>

<div class="member-card card animate-fadeIn">
  <div class="member-header">
    <img 
      src={member.avatar} 
      alt={member.name}
      class="member-avatar"
      loading="lazy"
    />
    <div class="member-info">
      <h3 class="member-name">{member.name}</h3>
      <p class="member-discord">@{member.discordName}</p>
      <p class="member-role">{member.role}</p>
    </div>
  </div>
  
  <div class="member-bio">
    <p>{member.bio}</p>
  </div>
  
  <div class="member-catchphrase">
    <strong>Signature Move:</strong> "{member.catchphrase}"
  </div>
  
  <div class="member-birthday">
    <span class="birthday-icon">🎂</span>
    <span>Birthday: {formatDate(member.birthday)}</span>
  </div>
  
  <div class="member-actions">
    <button 
      class="action-button" 
      class:active={showQuotes}
      onclick={toggleQuotes}
    >
      💬 Quotes ({member.favoriteQuotes.length})
    </button>
    
    <button 
      class="action-button"
      class:active={showAchievements}
      onclick={toggleAchievements}
    >
      🏆 Badges ({member.achievements.length})
    </button>
  </div>
  
  {#if showQuotes}
    <div class="quotes-section animate-slideIn">
      <h4>Legendary Quotes</h4>
      <ul class="quotes-list">
        {#each member.favoriteQuotes as quote}
          <li class="quote-item">"{quote}"</li>
        {/each}
      </ul>
    </div>
  {/if}
  
  {#if showAchievements}
    <div class="achievements-section animate-slideIn">
      <h4>Achievements</h4>
      <div class="achievements-grid">
        {#each member.achievements as achievement}
          <div class="achievement-badge">
            <span class="achievement-icon">{achievement.icon}</span>
            <div class="achievement-info">
              <strong>{achievement.name}</strong>
              <p>{achievement.description}</p>
              <small>Earned: {formatDate(achievement.earnedDate)}</small>
            </div>
          </div>
        {/each}
      </div>
    </div>
  {/if}
</div>

<style>
  .member-card {
    position: relative;
    overflow: hidden;
  }
  
  .member-card::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 4px;
    background: linear-gradient(90deg, var(--color-primary), var(--color-accent));
    opacity: 0;
    transition: opacity var(--transition-base);
  }
  
  .member-card:hover::before {
    opacity: 1;
  }
  
  .member-header {
    display: flex;
    gap: var(--space-md);
    margin-bottom: var(--space-lg);
  }
  
  .member-avatar {
    width: 80px;
    height: 80px;
    border-radius: var(--radius-xl);
    object-fit: cover;
    border: 3px solid var(--color-border);
    transition: transform var(--transition-base);
  }
  
  .member-card:hover .member-avatar {
    transform: scale(1.05);
  }
  
  .member-info {
    flex: 1;
  }
  
  .member-name {
    margin: 0 0 var(--space-xs) 0;
    color: var(--color-text);
  }
  
  .member-discord {
    margin: 0 0 var(--space-xs) 0;
    color: var(--color-primary);
    font-weight: 600;
    font-family: var(--font-mono);
  }
  
  .member-role {
    margin: 0;
    color: var(--color-accent);
    font-weight: 500;
    font-style: italic;
  }
  
  .member-bio {
    margin-bottom: var(--space-lg);
    color: var(--color-text-secondary);
    line-height: 1.6;
  }
  
  .member-catchphrase {
    margin-bottom: var(--space-lg);
    padding: var(--space-md);
    background: var(--color-bg-tertiary);
    border-radius: var(--radius-md);
    border-left: 4px solid var(--color-primary);
    font-style: italic;
  }
  
  .member-birthday {
    display: flex;
    align-items: center;
    gap: var(--space-sm);
    margin-bottom: var(--space-lg);
    color: var(--color-text-secondary);
  }
  
  .birthday-icon {
    font-size: var(--text-lg);
  }
  
  .member-actions {
    display: flex;
    gap: var(--space-sm);
    margin-bottom: var(--space-lg);
  }
  
  .action-button {
    flex: 1;
    padding: var(--space-sm) var(--space-md);
    background: var(--color-bg-tertiary);
    border: 1px solid var(--color-border);
    border-radius: var(--radius-md);
    color: var(--color-text);
    cursor: pointer;
    transition: all var(--transition-fast);
    font-size: var(--text-sm);
  }
  
  .action-button:hover,
  .action-button.active {
    background: var(--color-primary);
    color: white;
    border-color: var(--color-primary);
  }
  
  .quotes-section,
  .achievements-section {
    margin-top: var(--space-lg);
    padding-top: var(--space-lg);
    border-top: 1px solid var(--color-border);
  }
  
  .quotes-section h4,
  .achievements-section h4 {
    margin-bottom: var(--space-md);
    color: var(--color-text);
  }
  
  .quotes-list {
    list-style: none;
    padding: 0;
    margin: 0;
  }
  
  .quote-item {
    padding: var(--space-sm) var(--space-md);
    margin-bottom: var(--space-sm);
    background: var(--color-bg-tertiary);
    border-radius: var(--radius-md);
    color: var(--color-text-secondary);
    font-style: italic;
    position: relative;
  }
  
  .quote-item::before {
    content: '"';
    position: absolute;
    left: var(--space-xs);
    top: var(--space-xs);
    font-size: var(--text-lg);
    color: var(--color-primary);
    font-weight: bold;
  }
  
  .achievements-grid {
    display: grid;
    gap: var(--space-md);
  }
  
  .achievement-badge {
    display: flex;
    gap: var(--space-sm);
    align-items: center;
    padding: var(--space-sm);
    background: var(--color-bg-tertiary);
    border-radius: var(--radius-md);
    transition: transform var(--transition-fast);
  }
  
  .achievement-badge:hover {
    transform: translateX(4px);
  }
  
  .achievement-icon {
    font-size: var(--text-2xl);
    flex-shrink: 0;
  }
  
  .achievement-info {
    flex: 1;
  }
  
  .achievement-info strong {
    color: var(--color-text);
    display: block;
    margin-bottom: var(--space-xs);
  }
  
  .achievement-info p {
    margin: 0 0 var(--space-xs) 0;
    color: var(--color-text-secondary);
    font-size: var(--text-sm);
  }
  
  .achievement-info small {
    color: var(--color-text-tertiary);
    font-size: var(--text-xs);
  }
  
  @media (max-width: 768px) {
    .member-header {
      flex-direction: column;
      text-align: center;
    }
    
    .member-avatar {
      align-self: center;
    }
    
    .member-actions {
      flex-direction: column;
    }
    
    .achievements-grid {
      grid-template-columns: 1fr;
    }
  }
</style>