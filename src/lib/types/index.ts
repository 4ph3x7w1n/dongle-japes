export interface Member {
  id: string;
  name: string;
  discordName: string;
  avatar: string;
  bio: string;
  role: string;
  catchphrase: string;
  favoriteQuotes: string[];
  birthday: string;
  joinDate: string;
  achievements: Achievement[];
}

export interface Achievement {
  id: string;
  name: string;
  description: string;
  icon: string;
  earnedDate: string;
}

export interface MusicLeagueRound {
  id: string;
  theme: string;
  date: string;
  winner: string;
  submissions: MusicSubmission[];
  playlistUrl?: string;
}

export interface MusicSubmission {
  memberId: string;
  song: string;
  artist: string;
  votes: number;
  comments: string[];
}

export interface Event {
  id: string;
  title: string;
  date: string;
  type: 'hangout' | 'game-night' | 'movie-night' | 'special';
  description: string;
  attendees: string[];
  location?: string;
  photos?: string[];
}

export interface LoreEntry {
  id: string;
  title: string;
  date: string;
  type: 'joke' | 'moment' | 'quote' | 'incident';
  description: string;
  involvedMembers: string[];
  media?: string[];
}

export interface DiscordStats {
  totalMessages: number;
  topEmojis: EmojiStat[];
  topChannels: ChannelStat[];
  voiceHours: number;
  serverCreated: string;
  memberCount: number;
}

export interface EmojiStat {
  emoji: string;
  name: string;
  count: number;
}

export interface ChannelStat {
  name: string;
  messageCount: number;
  lastActive: string;
}