export type Theme = 'dark' | 'clean' | 'power' | 'spirit';
export const designs = [
 { key: 'dark', label: 'Dark Athletic', description: 'Die bisherige Variante', descriptionIt: 'La versione attuale' },
 { key: 'power', label: 'Power Play', description: 'Diagonal. Kraftvoll. Direkt.', descriptionIt: 'Diagonale. Energica. Diretta.' },
 { key: 'spirit', label: 'Team Spirit', description: 'Lebendig. Nahbar. Gemeinsam.', descriptionIt: 'Vivace. Accogliente. Insieme.' },
] as const;
