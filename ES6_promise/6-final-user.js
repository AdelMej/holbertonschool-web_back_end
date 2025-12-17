import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const result = await Promise.allSettled([
    signUpUser(firstName, lastName),
    uploadPhoto(fileName),
  ]);

  return result.map((promise) => {
    if (promise.status === 'fulfilled') {
      return {
        status: promise.status,
        value: promise.value,
      };
    }
    return {
      status: promise.status,
      value: promise.reason.message,
    };
  });
}
