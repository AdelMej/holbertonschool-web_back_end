export default async function handleResponseFromApi(promise) {
  try {
    await promise;
    console.log('Got a response from the API');
  } catch (err) {
    return Error();
  }
}
