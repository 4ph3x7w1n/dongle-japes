import type { DiscordStats } from '$lib/types';

export const discordStats: DiscordStats = {
  totalMessages: 142069,
  topEmojis: [
    { emoji: '🌮', name: 'taco', count: 3847 },
    { emoji: '💀', name: 'skull', count: 2910 },
    { emoji: '🤔', name: 'thinking', count: 2156 },
    { emoji: '😂', name: 'joy', count: 1893 },
    { emoji: '🎮', name: 'video_game', count: 1420 },
    { emoji: '🍕', name: 'pizza', count: 1337 },
    { emoji: '👑', name: 'crown', count: 1111 },
    { emoji: '🔥', name: 'fire', count: 999 }
  ],
  topChannels: [
    { name: 'general-chaos', messageCount: 45230, lastActive: '2024-01-15' },
    { name: 'music-league', messageCount: 23410, lastActive: '2024-01-14' },
    { name: 'food-discourse', messageCount: 19847, lastActive: '2024-01-15' },
    { name: 'gaming-dungeon', messageCount: 15666, lastActive: '2024-01-13' },
    { name: 'meme-vault', messageCount: 12890, lastActive: '2024-01-15' }
  ],
  voiceHours: 2847,
  serverCreated: '2020-03-01',
  memberCount: 4
};