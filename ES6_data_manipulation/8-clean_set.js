export default function cleanSet(set, startString) {
  if (!startString || !typeof startString === 'string') return '';

  const result = [];

  for (const value of set) {
    // eslint-disable-next-line no-continue
    if (!value.startsWith(startString)) continue;
    result.push(value.slice(startString.length));
  }

  return result.join('-');
}
