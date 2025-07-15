import type { Event } from '$lib/types';

export const events: Event[] = [
  {
    id: 'game-night-1',
    title: 'Dongle Game Night: Jackbox Edition',
    date: '2024-02-10',
    type: 'game-night',
    description: 'Monthly game night featuring Jackbox games and inevitable chaos',
    attendees: ['max', 'adam', 'chris', 'dylan'],
    location: 'Discord Voice Chat',
    photos: []
  },
  {
    id: 'taco-tuesday-1',
    title: 'Taco Tuesday Pilgrimage',
    date: '2024-02-13',
    type: 'hangout',
    description: 'Dylan leads the group to his latest taco truck discovery',
    attendees: ['dylan', 'max', 'chris'],
    location: 'El Primo Taco Truck',
    photos: []
  },
  {
    id: 'movie-night-1',
    title: 'Bad Movie Night: The Room',
    date: '2024-02-17',
    type: 'movie-night',
    description: 'Watching The Room with live Discord commentary',
    attendees: ['adam', 'max', 'chris', 'dylan'],
    location: 'Discord Screen Share',
    photos: []
  },
  {
    id: 'anniversary-1',
    title: 'Dongle Japes 4th Anniversary',
    date: '2024-03-01',
    type: 'special',
    description: 'Celebrating 4 years of friendship and terrible jokes',
    attendees: ['max', 'adam', 'chris', 'dylan'],
    location: 'TBD',
    photos: []
  },
  {
    id: 'lan-party-1',
    title: 'Retro LAN Party',
    date: '2024-03-15',
    type: 'game-night',
    description: 'Old school LAN party with Age of Empires and Unreal Tournament',
    attendees: ['max', 'adam', 'chris'],
    location: 'Max\'s Place',
    photos: []
  }
];