export default async function handleResponseFromApi(promise) {
  try {
    await promise;
    console.log('Got a response from the API');
    return {
      status: 200,
      body: 'success',
    };
  } catch (err) {
    return Error();
  }
}
