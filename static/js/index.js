let url = 'http://127.0.0.1:8000/window/quote/';

const getQuoteWindow = async () => {
  let estiloVentana = document.getElementById("estiloVentana").value;
  let ancho = document.getElementById("Ancho").value;
  let alto = document.getElementById("Alto").value;
  let acabadoAluminio = document.getElementById("AcabadoAluminio").value;
  let tipoVidrio = document.getElementById("TipoVidrio").value;
  let numeroVentanasCotizar = document.getElementById("NoUnidades").value;
  let vidrioEsmerilado = document.getElementById("flexCheckDefault").checked;

  let resultadoCotizacion = document.getElementById("ResultadoCotizacion");

  const data = {
    estilo_ventana: estiloVentana,
    ancho: ancho,
    alto: alto,
    acabado_aluminio: acabadoAluminio,
    tipo_vidrio: tipoVidrio,
    vidrio_esmerilado: vidrioEsmerilado,
    numero_ventanas_cotizar: numeroVentanasCotizar,
  }

  const options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
  };

  await fetch(url, options)
    .then(response => response.json())
    .then(data => {
      resultadoCotizacion.value = data.result;
    })
    .catch(error => {
      console.error('Error al hacer la petición:', error);
    });
}