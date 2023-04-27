
const FormGeneral = () => {

  const [windowStyle, setWindowStyle] = React.useState("");
  const [windowWidth, setWindowWidth] = React.useState("");
  const [windowHeight, setWindowHeight] = React.useState("");
  const [aluminumFinishes, setAluminumFinishes] = React.useState("");
  const [typeGlass, setTypeGlass] = React.useState("");
  const [glassFrosted, setGlassFrosted] = React.useState(false);
  const [numWindowQuote, setNumWindowQuote] = React.useState("");
  const [resultQuote, setResultQuote] = React.useState("");

  const [listWindowStyles, setListWindowStyles] = React.useState([]);
  const [listAluminumFinishes, setListAluminumFinishes] = React.useState([]);
  const [listTypeGlass, setListTypeGlass] = React.useState([]);

  const getQuoteWindow = async () => {
    const data = {
      window_style: windowStyle,
      window_width: windowWidth,
      window_height: windowHeight,
      aluminum_finishes: aluminumFinishes,
      type_glass: typeGlass,
      glass_frosted: glassFrosted,
      num_window_quote: numWindowQuote,
    }

    return data
  }

  return (
    <React.Fragment>
      <div className="dimensions-window">
        <div className="mb-3 row">
          <label for="Ancho" className="col-sm-2 col-form-label">Ancho</label>
          <div className="col-sm-9">
            <input type="text" className="form-control" id="Ancho" />
          </div>
        </div>
        <div className="mb-3 row">
          <label for="Alto" className="col-sm-2 col-form-label">Alto</label>
          <div className="col-sm-9">
            <input type="text" className="form-control" id="Alto" />
          </div>
        </div>
      </div>
      <div className="mb-3">
        <label for="EstiloVentana" className="form-label">Estilo de la ventana</label>
        <select className="form-select" aria-label="Default select example" id="estiloVentana">
          <option value="0" selected>- seleccione -</option>
          {listWindowStyles.map((element) => (
            <option value="{{element.name}}">{element.name}</option>
          ))}
        </select>
      </div>
      <div className="mb-3">
        <label for="AcabadoAluminio" className="form-label">Acabado del aluminio</label>
        <select className="form-select" aria-label="Default select example" id="AcabadoAluminio">
          <option value="0" selected>- seleccione -</option>
          {listAluminumFinishes.map((element) => (
            <option value="{{element.id}}">{element.name} / $ {element.price}</option>
          ))}
        </select>
      </div>
      <div className="mb-3">
        <label for="TipoVidrio" className="form-label">Tipo del Vidrio</label>
        <select className="form-select" aria-label="Default select example" id="TipoVidrio">
          <option value="0" selected>- seleccione -</option>
          {listTypeGlass.map((element) => (
            <option value="{{element.id}}">{element.name} / $ {element.price}</option>
          ))}
        </select>
      </div>
      <div className="form-check">
        <input className="form-check-input" type="checkbox" value="" id="flexCheckDefault" />
        <label className="form-check-label" for="flexCheckDefault">
          Vidrio Esmerilizado
        </label>
      </div>
      <br
      />
      <div className="mb-3 row">
        <label for="NoUnidades" className="col-sm-3 col-form-label">No unidades</label>
        <div className="col-sm-9">
          <input type="text" className="form-control" id="NoUnidades" />
        </div>
      </div>
      <hr />
      <div className="mb-3 row">
        <label for="ResultadoCotizacion" className="col-sm-5 col-form-label"><b>Resultado Cotización</b></label>
        <div className="col-sm-7">
          <input type="text" className="form-control" id="ResultadoCotizacion" disabled />
        </div>
      </div>
      <div className="col-lg-10 btn-group" role="group" aria-label="Basic example">
        <button type="button" className="btn btn-primary">Limpiar</button>
        <button onclick="" type="button" className="btn btn-primary">Solicitar</button>
        <button onclick="" type="button" className="btn btn-primary ml-auto"><i className='bx bx-right-arrow-alt'></i></button>
      </div>
    </React.Fragment>
  )
}


const ListItemQuote = () => {

  const url = 'http://127.0.0.1:8000/window/quote/';
  const [listItemCuote, setListItemCuote] = React.useState([])
  const [sumPrice, setSumPrice] = React.useState(0);

  React.useEffect(() => {
    const prices = listItemCuote.map(obj => obj.price);
    const totalPrice = prices.reduce((sum, price) => sum + price, 0);
    const formattedPrice = totalPrice.toLocaleString("es-AR");
    setSumPrice(formattedPrice);
  }, [listItemCuote])

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
            {listItemCuote.map(item =>
            (<tr key={item.id}>
              <th scope="row">{item.id}</th>
              <td>{item.name}</td>
              <td>{item.quantity}</td>
              <td>{item.price}</td>
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
      </div>
    </React.Fragment>
  )
}

const App = () => {

  return (
    <React.Fragment>
      {/* <!-- Board Control Quote --> */}
      <div class="content-form-price" id="FormGeneral">
        <FormGeneral />
      </div>
      {/* <!-- Quote made --> */}
      <div class="mt-5 list-items-quote">
        <h4>Lista de articulos cotizados</h4>
        <div id="ListItemQuote">
          <ListItemQuote />
        </div>
      </div>
    </React.Fragment>
  )
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
);