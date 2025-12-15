export default function createInt8TypedArray(length, position, value) {
  if (position > length - 1) {
    throw Error('Position outside range');
  }

  const array = new Uint8Array(length);
  array[position] = value;
  return array;
}
