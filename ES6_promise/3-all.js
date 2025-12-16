import { uploadPhoto, createUser } from './utils.js';

export default async function handleProfileSignup() {
  try {
    const result = await Promise.all([uploadPhoto(), createUser()]);
    console.log(`${result[0].body} ${result[1].firstName} ${result[1].lastName}`);
  } catch (err) {
    console.log('Signup system offline');
  }
}
