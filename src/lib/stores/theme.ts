import { writable } from 'svelte/store';

type Theme = 'light' | 'dark';

function createThemeStore() {
  const defaultTheme: Theme = 'dark';
  const isBrowser = typeof window !== 'undefined';
  const stored = isBrowser ? localStorage.getItem('theme') as Theme : null;
  const initialTheme = stored || defaultTheme;

  const { subscribe, set, update } = writable<Theme>(initialTheme);

  return {
    subscribe,
    toggle: () => {
      update(theme => {
        const newTheme = theme === 'light' ? 'dark' : 'light';
        if (isBrowser) {
          localStorage.setItem('theme', newTheme);
          document.documentElement.setAttribute('data-theme', newTheme);
        }
        return newTheme;
      });
    },
    set: (theme: Theme) => {
      if (isBrowser) {
        localStorage.setItem('theme', theme);
        document.documentElement.setAttribute('data-theme', theme);
      }
      set(theme);
    },
    init: () => {
      if (isBrowser) {
        const stored = localStorage.getItem('theme') as Theme;
        const theme = stored || defaultTheme;
        document.documentElement.setAttribute('data-theme', theme);
        set(theme);
      }
    }
  };
}

export const theme = createThemeStore();