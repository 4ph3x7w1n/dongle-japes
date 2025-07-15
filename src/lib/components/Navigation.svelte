<script lang="ts">
  import { theme } from '$lib/stores/theme';
  import { onMount } from 'svelte';
  
  let isScrolled = $state(false);
  let mobileMenuOpen = $state(false);
  
  const navItems = [
    { href: '#home', label: 'Home' },
    { href: '#about', label: 'About' },
    { href: '#lore', label: 'Lore' },
    { href: '#music', label: 'Music League' },
    { href: '#events', label: 'Events' },
    { href: '#birthdays', label: 'Birthdays' },
    { href: '#discord', label: 'Discord' },
    { href: '#gallery', label: 'Gallery' },
    { href: '#contact', label: 'Join Us' },
  ];
  
  function handleScroll() {
    isScrolled = window.scrollY > 10;
  }
  
  function toggleMobileMenu() {
    mobileMenuOpen = !mobileMenuOpen;
  }
  
  function closeMobileMenu() {
    mobileMenuOpen = false;
  }
  
  onMount(() => {
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  });
</script>

<nav class="nav" class:scrolled={isScrolled}>
  <div class="container nav-container">
    <a href="#home" class="logo" onclick={closeMobileMenu}>
      <span class="logo-icon">🎮</span>
      <span class="logo-text">The Dongle Japes</span>
    </a>
    
    <button 
      class="mobile-toggle"
      onclick={toggleMobileMenu}
      aria-label="Toggle navigation"
    >
      <span class="hamburger" class:active={mobileMenuOpen}></span>
    </button>
    
    <div class="nav-menu" class:open={mobileMenuOpen}>
      <ul class="nav-links">
        {#each navItems as item}
          <li>
            <a 
              href={item.href} 
              class="nav-link"
              onclick={closeMobileMenu}
            >
              {item.label}
            </a>
          </li>
        {/each}
      </ul>
      
      <button 
        class="theme-toggle"
        onclick={() => theme.toggle()}
        aria-label="Toggle theme"
      >
        {#if $theme === 'dark'}
          <svg width="20" height="20" fill="currentColor" viewBox="0 0 20 20">
            <path d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.706.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.465 5.05l-.708-.707a1 1 0 00-1.414 1.414l.707.707zm1.414 8.486l-.707.707a1 1 0 01-1.414-1.414l.707-.707a1 1 0 011.414 1.414zM4 11a1 1 0 100-2H3a1 1 0 000 2h1z" />
          </svg>
        {:else}
          <svg width="20" height="20" fill="currentColor" viewBox="0 0 20 20">
            <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z" />
          </svg>
        {/if}
      </button>
    </div>
  </div>
</nav>

<style>
  .nav {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    z-index: 1000;
    background: var(--color-bg);
    border-bottom: 1px solid transparent;
    transition: all var(--transition-base);
  }
  
  .nav.scrolled {
    background: var(--color-bg-secondary);
    border-bottom-color: var(--color-border);
    box-shadow: 0 2px 10px var(--color-shadow);
  }
  
  .nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    height: 4rem;
  }
  
  .logo {
    display: flex;
    align-items: center;
    gap: var(--space-sm);
    font-weight: 700;
    font-size: var(--text-xl);
    color: var(--color-text);
    text-decoration: none;
  }
  
  .logo-icon {
    font-size: var(--text-2xl);
  }
  
  .logo:hover {
    color: var(--color-primary);
    text-decoration: none;
  }
  
  .nav-menu {
    display: flex;
    align-items: center;
    gap: var(--space-xl);
  }
  
  .nav-links {
    display: flex;
    gap: var(--space-lg);
    list-style: none;
    margin: 0;
    padding: 0;
  }
  
  .nav-link {
    color: var(--color-text);
    font-weight: 500;
    transition: color var(--transition-fast);
    position: relative;
  }
  
  .nav-link:hover {
    color: var(--color-primary);
    text-decoration: none;
  }
  
  .nav-link::after {
    content: '';
    position: absolute;
    bottom: -4px;
    left: 0;
    right: 0;
    height: 2px;
    background: var(--color-primary);
    transform: scaleX(0);
    transition: transform var(--transition-base);
  }
  
  .nav-link:hover::after {
    transform: scaleX(1);
  }
  
  .theme-toggle {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    border: none;
    background: var(--color-bg-tertiary);
    color: var(--color-text);
    border-radius: var(--radius-full);
    cursor: pointer;
    transition: all var(--transition-fast);
  }
  
  .theme-toggle:hover {
    background: var(--color-primary);
    color: white;
    transform: rotate(180deg);
  }
  
  .mobile-toggle {
    display: none;
    background: none;
    border: none;
    cursor: pointer;
    padding: var(--space-sm);
  }
  
  .hamburger {
    display: block;
    width: 24px;
    height: 2px;
    background: var(--color-text);
    position: relative;
    transition: all var(--transition-base);
  }
  
  .hamburger::before,
  .hamburger::after {
    content: '';
    position: absolute;
    width: 100%;
    height: 100%;
    background: var(--color-text);
    transition: all var(--transition-base);
  }
  
  .hamburger::before {
    transform: translateY(-8px);
  }
  
  .hamburger::after {
    transform: translateY(8px);
  }
  
  .hamburger.active {
    background: transparent;
  }
  
  .hamburger.active::before {
    transform: rotate(45deg);
  }
  
  .hamburger.active::after {
    transform: rotate(-45deg);
  }
  
  @media (max-width: 768px) {
    .mobile-toggle {
      display: block;
    }
    
    .nav-menu {
      position: fixed;
      top: 4rem;
      left: 0;
      right: 0;
      background: var(--color-bg);
      border-bottom: 1px solid var(--color-border);
      padding: var(--space-lg);
      flex-direction: column;
      transform: translateY(-100%);
      opacity: 0;
      pointer-events: none;
      transition: all var(--transition-base);
    }
    
    .nav-menu.open {
      transform: translateY(0);
      opacity: 1;
      pointer-events: auto;
    }
    
    .nav-links {
      flex-direction: column;
      width: 100%;
      text-align: center;
    }
    
    .nav-link::after {
      display: none;
    }
  }
</style>