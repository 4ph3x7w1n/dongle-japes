import type { Member } from '$lib/types';

export const members: Member[] = [
  {
    id: 'max',
    name: 'Max',
    discordName: 'BamBurrg',
    avatar: '/pics/max.png',
    bio: 'The visionary founder of The Dongle Japes. Known for his legendary hot takes and unmatched ability to derail any conversation.',
    role: 'Chaos Architect',
    catchphrase: 'But what if we just...',
    favoriteQuotes: [
      'I\'m not saying it\'s a good idea, but...',
      'Hear me out...',
      'This is the way'
    ],
    birthday: '1995-06-15',
    joinDate: '2020-03-01',
    achievements: [
      {
        id: 'founder',
        name: 'Founding Father',
        description: 'Created The Dongle Japes',
        icon: '👑',
        earnedDate: '2020-03-01'
      },
      {
        id: 'music-champion',
        name: 'Music League Champion',
        description: 'Won 10 Music League rounds',
        icon: '🏆',
        earnedDate: '2023-08-15'
      }
    ]
  },
  {
    id: 'adam',
    name: 'Adam',
    discordName: 'Chuck Shoulders',
    avatar: '/pics/adam.jpg',
    bio: 'The group\'s resident meme lord and GIF connoisseur. If there\'s a reaction image for it, Chuck has it ready.',
    role: 'Meme Curator',
    catchphrase: '*posts perfect reaction GIF*',
    favoriteQuotes: [
      'Actually, that reminds me of this one time...',
      'I have the perfect GIF for this',
      'Based and dongle-pilled'
    ],
    birthday: '1994-11-22',
    joinDate: '2020-03-01',
    achievements: [
      {
        id: 'gif-master',
        name: 'GIF Master',
        description: 'Posted 1000+ reaction GIFs',
        icon: '🎬',
        earnedDate: '2022-05-10'
      },
      {
        id: 'night-owl',
        name: 'Night Owl',
        description: 'Most active during 2-4 AM',
        icon: '🦉',
        earnedDate: '2021-09-20'
      }
    ]
  },
  {
    id: 'chris',
    name: 'Chris',
    discordName: 'Bruh',
    avatar: '/pics/chris.png',
    bio: 'Master of the one-word response. Chris\'s "bruh" has more meanings than an ancient hieroglyph.',
    role: 'Vibe Checker',
    catchphrase: 'Bruh...',
    favoriteQuotes: [
      'Bruh',
      'That\'s crazy',
      'No cap fr fr'
    ],
    birthday: '1996-03-08',
    joinDate: '2020-03-15',
    achievements: [
      {
        id: 'minimalist',
        name: 'Minimalist',
        description: 'Sent 100 one-word messages in a row',
        icon: '📝',
        earnedDate: '2021-12-01'
      },
      {
        id: 'vibe-check',
        name: 'Vibe Inspector',
        description: 'Successfully called out bad vibes 50 times',
        icon: '✅',
        earnedDate: '2023-02-14'
      }
    ]
  },
  {
    id: 'dylan',
    name: 'Dylan',
    discordName: 'OFfDutyTacoTruck',
    avatar: '/pics/dylan.png',
    bio: 'The group\'s culinary expert and late-night philosopher. Always knows where to find the best tacos at 3 AM.',
    role: 'Taco Evangelist',
    catchphrase: 'You know what would slap right now? Tacos.',
    favoriteQuotes: [
      'I\'m not saying tacos solve everything, but...',
      'This conversation needs more hot sauce',
      'Food truck > restaurant, fight me'
    ],
    birthday: '1995-09-30',
    joinDate: '2020-04-01',
    achievements: [
      {
        id: 'foodie',
        name: 'Certified Foodie',
        description: 'Recommended 50+ food spots',
        icon: '🌮',
        earnedDate: '2022-07-20'
      },
      {
        id: 'philosopher',
        name: 'Midnight Philosopher',
        description: 'Started 20 deep conversations after midnight',
        icon: '🤔',
        earnedDate: '2023-11-05'
      }
    ]
  }
];