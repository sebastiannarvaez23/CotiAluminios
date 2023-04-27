const options = {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify(data)
};

const getResultQuote = async (data) => {
  const url = "";
  await fetch(url, options)
    .then(response => response.json())
    .then(data => {
      resultadoCotizacion.value = data.result;
    })
    .catch(error => {
      console.error('Error al hacer la petición:', error);
    });
}