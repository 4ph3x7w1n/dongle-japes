import type { MusicLeagueRound } from '$lib/types';

export const musicLeagueRounds: MusicLeagueRound[] = [
  {
    id: 'round-1',
    theme: 'Songs That Make You Cry',
    date: '2023-03-10',
    winner: 'chris',
    playlistUrl: 'https://open.spotify.com/playlist/YOUR_PLAYLIST_ID',
    submissions: [
      {
        memberId: 'chris',
        song: 'Never Gonna Give You Up',
        artist: 'Rick Astley',
        votes: 12,
        comments: ['Legendary move', 'I hate that this works', 'Crying from laughter counts']
      },
      {
        memberId: 'max',
        song: 'Hurt',
        artist: 'Johnny Cash',
        votes: 8,
        comments: ['Too real', 'Max going for the jugular']
      },
      {
        memberId: 'adam',
        song: 'Mad World',
        artist: 'Gary Jules',
        votes: 6,
        comments: ['Classic Chuck pick', 'Donnie Darko vibes']
      },
      {
        memberId: 'dylan',
        song: 'The Scientist',
        artist: 'Coldplay',
        votes: 5,
        comments: ['Dylan in his feels', 'Pairs well with tacos']
      }
    ]
  },
  {
    id: 'round-2',
    theme: 'Songs to Eat Tacos To',
    date: '2023-04-15',
    winner: 'dylan',
    playlistUrl: 'https://open.spotify.com/playlist/YOUR_PLAYLIST_ID',
    submissions: [
      {
        memberId: 'dylan',
        song: 'Tequila',
        artist: 'The Champs',
        votes: 11,
        comments: ['Dylan\'s in his element', 'Perfect', 'This is the way']
      },
      {
        memberId: 'max',
        song: 'Mexican Radio',
        artist: 'Wall of Voodoo',
        votes: 7,
        comments: ['Solid choice', 'Max knows the assignment']
      },
      {
        memberId: 'chris',
        song: 'Hot Hot Hot',
        artist: 'Arrow',
        votes: 6,
        comments: ['Bruh', 'Chris with the heat']
      },
      {
        memberId: 'adam',
        song: 'Low Rider',
        artist: 'War',
        votes: 9,
        comments: ['Chuck coming through', 'Cruising for tacos']
      }
    ]
  },
  {
    id: 'round-3',
    theme: '3 AM Vibes',
    date: '2023-05-20',
    winner: 'adam',
    playlistUrl: 'https://open.spotify.com/playlist/YOUR_PLAYLIST_ID',
    submissions: [
      {
        memberId: 'adam',
        song: 'Nightcall',
        artist: 'Kavinsky',
        votes: 10,
        comments: ['Chuck knows the night', 'Drive soundtrack ftw', 'Perfect 3 AM energy']
      },
      {
        memberId: 'max',
        song: 'Midnight City',
        artist: 'M83',
        votes: 8,
        comments: ['Max with the synths', 'Saxophone moment']
      },
      {
        memberId: 'dylan',
        song: 'Day \'n\' Nite',
        artist: 'Kid Cudi',
        votes: 9,
        comments: ['Dylan philosophizing', 'Taco truck hours']
      },
      {
        memberId: 'chris',
        song: '4 AM',
        artist: '2 Chainz',
        votes: 5,
        comments: ['Literally 4 AM', 'Chris keeping it real']
      }
    ]
  }
];