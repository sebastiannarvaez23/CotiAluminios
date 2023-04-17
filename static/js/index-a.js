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

/* Modals bootstrap */

$('#exampleModal').on('show.bs.modal', function (event) {
  var button = $(event.relatedTarget) // Button that triggered the modal
  var recipient = button.data('whatever') // Extract info from data-* attributes
  // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
  // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
  var modal = $(this)
  modal.find('.modal-title').text('New message to ' + recipient)
  modal.find('.modal-body input').val(recipient)
})