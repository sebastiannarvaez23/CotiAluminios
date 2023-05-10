
const FormGeneral = (props) => {

  const [windowWidth, setWindowWidth] = React.useState("");
  const [windowHeight, setWindowHeight] = React.useState("");
  const [windowStyle, setWindowStyle] = React.useState("");
  const [aluminumFinishes, setAluminumFinishes] = React.useState("");
  const [typeGlass, setTypeGlass] = React.useState("");
  const [glassFrosted, setGlassFrosted] = React.useState(false);
  const [numWindowQuote, setNumWindowQuote] = React.useState("");
  const [quote, setQuote] = React.useState({
    name: "",
    quantity: "",
    price: ""
  });

  const [listWindowStyles, setListWindowStyles] = React.useState([]);
  const [listAluminumFinishes, setListAluminumFinishes] = React.useState([]);
  const [listTypeGlass, setListTypeGlass] = React.useState([]);

  const getConfAPI = (data) => {
    return {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    };
  }

  const getListAluminumFinishes = async () => {
    const url = "/api/aluminumfinishes/";

    await fetch(url, { method: 'GET', headers: { 'Content-Type': 'application/json' } })
      .then(response => response.json())
      .then(data => {
        setListAluminumFinishes(data.aluminum_finishes);
      })
      .catch(error => {
        console.error('Error al hacer la petición:', error);
      });
  }

  const getListTypeGlass = async () => {
    const url = "/api/typeglass/";

    await fetch(url, { method: 'GET', headers: { 'Content-Type': 'application/json' } })
      .then(response => response.json())
      .then(data => {
        setListTypeGlass(data.type_glass);
      })
      .catch(error => {
        console.error('Error al hacer la petición:', error);
      });
  }

  const getListWindowStyles = async () => {
    const url = "/api/windowstyles/";

    await fetch(url, { method: 'GET', headers: { 'Content-Type': 'application/json' } })
      .then(response => response.json())
      .then(data => {
        setListWindowStyles(data.styles_window);
      })
      .catch(error => {
        console.error('Error al hacer la petición:', error);
      });
  }

  const getResultQuote = async () => {

    const data = {
      window_style: windowStyle,
      window_width: windowWidth,
      window_height: windowHeight,
      aluminum_finishes: aluminumFinishes,
      type_glass: typeGlass,
      glass_frosted: glassFrosted,
      num_window_quote: numWindowQuote,
    }

    const url = "/api/quote/";
    const conf = getConfAPI(data);

    await fetch(url, conf)
      .then(response => response.json())
      .then(data => {
        if (data.status_code == 200) {
          props.setResultQuote(data.data.result);
          setQuote(data.data)
        } else if (data.status_code == 400) {

          const Toast = Swal.mixin({
            toast: true,
            position: 'top-right',
            showConfirmButton: false,
            timer: 4000,
            timerProgressBar: true,
            didOpen: (toast) => {
              toast.addEventListener('mouseenter', Swal.stopTimer)
              toast.addEventListener('mouseleave', Swal.resumeTimer)
            }
          })

          Toast.fire({
            icon: 'error',
            title: data.message
          })
        }
      })
      .catch(error => {
        console.error('Error al hacer la petición:', error);
      });
  }

  const addItemQuote = (data) => {
    if (data.name === "" || data.name === null || data.name === undefined) { return };
    const arr = props.listItemQuote;
    arr.push(data)
    props.setListItemQuote(arr)
    props.setNumRowsItemQuote(props.numRowsItemQuote + 1)
    console.log(props.listItemQuote)
  }

  const clean_form = () => {
    setWindowWidth("");
    setWindowHeight("");
    setWindowStyle("");
    setAluminumFinishes("");
    setTypeGlass("");
    setGlassFrosted(false);
    setNumWindowQuote("");
    props.setResultQuote("");
  }

  React.useEffect(() => {
    getListWindowStyles();
    getListAluminumFinishes();
    getListTypeGlass();
  }, [])

  return (
    <React.Fragment>
      <div className="dimensions-window">
        <input type="hidden" name="csrfmiddlewaretoken" value="{% csrf_token %}" />
        <div className="mb-3 row">
          <label htmlFor="Ancho" className="col-sm-2 col-form-label">Ancho</label>
          <div className="col-sm-9">
            <input onChange={(e) => {
              const regex = /^\d{0,3}(\.\d{0,2})?$/;
              const newValue = e.target.value;
              if (regex.test(newValue)) {
                setWindowWidth(newValue);
              }
            }} type="text" value={windowWidth} className="form-control" id="Ancho" />
          </div>
        </div>
        <div className="mb-3 row">
          <label htmlFor="Alto" className="col-sm-2 col-form-label">Alto</label>
          <div className="col-sm-9">
            <input onChange={(event) => {
              const newValue = event.target.value;
              const regex = /^\d{0,3}(\.\d{0,2})?$/;
              if (regex.test(newValue)) {
                setWindowHeight(newValue);
              }
            }} type="text" value={windowHeight} className="form-control" id="Alto" />
          </div>
        </div>
      </div>
      <div className="mb-3">
        <label htmlFor="EstiloVentana" className="form-label">Estilo de la ventana</label>
        <select value={windowStyle} onChange={(e) => { setWindowStyle(e.target.value) }} className="form-select" aria-label="Default select example" id="estiloVentana">
          <option value="">- seleccione -</option>
          {listWindowStyles.map((element) => (
            <option key={element.id} value={element.id}>{element.name}</option>
          ))}
        </select>
      </div>
      <div className="mb-3">
        <label htmlFor="AcabadoAluminio" className="form-label">Acabado del aluminio</label>
        <select value={aluminumFinishes} onChange={(e) => { setAluminumFinishes(e.target.value) }} className="form-select" aria-label="Default select example" id="AcabadoAluminio">
          <option value="">- seleccione -</option>
          {listAluminumFinishes.map((element) => (
            <option key={element.id} value={element.id}>{element.name} / $ {element.price}</option>
          ))}
        </select>
      </div>
      <div className="mb-3">
        <label htmlFor="TipoVidrio" className="form-label">Tipo del Vidrio</label>
        <select value={typeGlass} onChange={(e) => { setTypeGlass(e.target.value) }} className="form-select" aria-label="Default select example" id="TipoVidrio">
          <option value="">- seleccione -</option>
          {listTypeGlass.map((element) => (
            <option key={element.id} value={element.id}>{element.name} / $ {element.price}</option>
          ))}
        </select>
      </div>
      <div className="form-check">
        <input checked={glassFrosted} onChange={(e) => { setGlassFrosted(!glassFrosted) }} className="form-check-input" type="checkbox" id="flexCheckDefault" />
        <label className="form-check-label" htmlFor="flexCheckDefault">
          Vidrio Esmerilizado
        </label>
      </div>
      <br
      />
      <div className="mb-3 row">
        <label htmlFor="NoUnidades" className="col-sm-3 col-form-label">No unidades</label>
        <div className="col-sm-9">
          <input onChange={(e) => {
            const newValue = e.target.value;
            const regex = /^\d{0,3}?$/;
            if (regex.test(newValue)) {
              setNumWindowQuote(newValue);
            }
          }} value={numWindowQuote} type="text" className="form-control" id="NoUnidades" />
        </div>
      </div>
      <hr />
      <div className="mb-3 row">
        <label htmlFor="ResultadoCotizacion" className="col-sm-5 col-form-label"><b>Resultado Cotización</b></label>
        <div className="col-sm-7">
          <input value={props.resultQuote} type="text" className="form-control" id="ResultadoCotizacion" disabled />
        </div>
      </div>
      <div className="col-lg-10 btn-group" role="group" aria-label="Basic example">
        <button onClick={clean_form} type="button" className="btn btn-primary">Limpiar</button>
        <button onClick={getResultQuote} type="button" className="btn btn-primary">Solicitar</button>
        <button onClick={() => {
          addItemQuote({
            id: props.numRowsItemQuote,
            name: quote.name,
            quantity: quote.quantity,
            price: quote.price
          })
        }} type="button" className="btn btn-primary ml-auto"><i className='bx bx-right-arrow-alt'></i></button>
      </div>
    </React.Fragment>
  )
}

const ListItemQuote = ({ listItemQuote, numRowsItemQuote, setListItemQuote }) => {

  const [sumPrice, setSumPrice] = React.useState(0);

  React.useEffect(() => {

    const prices = listItemQuote.map(obj => obj.price);
    const totalPrice = prices.reduce((sum, price) => sum + price, 0);
    const formattedPrice = totalPrice.toLocaleString("es-AR");
    setSumPrice(formattedPrice);

  }, [numRowsItemQuote])

  return (
    <React.Fragment>
      <div className="ListQuote">
        <table className="table">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Ventana</th>
              <th scope="col">Cantidad</th>
              <th scope="col">Precio</th>
            </tr>
          </thead>
          <tbody id="RowsQuote">
            {listItemQuote.map(item =>
            (<tr key={item.id}>
              <th scope="row">{item.id}</th>
              <td>{item.name}</td>
              <td>{item.quantity}</td>
              <td>{item.price.toLocaleString('es-CO', { style: 'currency', currency: 'COP' })}</td>
            </tr>)
            )}
          </tbody>
        </table>
      </div>
      <div>
        <hr />
        <div className="footer-quote">
          <h5>Total</h5><h5 className="value-quote">$ {sumPrice}</h5>
        </div>

        <button onClick={() => {
          setListItemQuote([]);
          setSumPrice(0)
        }} type="button" className="btn btn-primary">Limpiar</button>
        <button type="button" className="btn btn-primary mt-2">Descargar PDF</button>
      </div>
    </React.Fragment>
  )
}

const App = () => {

  const [resultQuote, setResultQuote] = React.useState("");
  const [listItemQuote, setListItemQuote] = React.useState([]);
  const [numRowsItemQuote, setNumRowsItemQuote] = React.useState(1);

  return (
    <React.Fragment>
      <div className="content-form-price" id="FormGeneral">
        <FormGeneral
          resultQuote={resultQuote}
          setResultQuote={setResultQuote}
          listItemQuote={listItemQuote}
          setListItemQuote={setListItemQuote}
          numRowsItemQuote={numRowsItemQuote}
          setNumRowsItemQuote={setNumRowsItemQuote}
        />
      </div>
      <div className="mt-5 list-items-quote">
        <h4>Lista de articulos cotizados</h4>
        <div id="ListItemQuote">
          <ListItemQuote
            listItemQuote={listItemQuote}
            setListItemQuote={setListItemQuote}
            numRowsItemQuote={numRowsItemQuote}
          />
        </div>
      </div>
    </React.Fragment>
  )
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
);