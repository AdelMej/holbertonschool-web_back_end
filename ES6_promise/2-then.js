export default async function handleResponseFromApi(promise) {
  try {
    await promise;
    return {
      status: 200,
      body: 'success',
    };
  } catch (err) {
    return Error();
  } finally {
    console.log('Got a response from the API');
  }
}
