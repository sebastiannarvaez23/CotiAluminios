const ListItemQuote = () => {

  const listItemCuote = [
    {
      id: 1,
      name: "window",
      quantity: 2,
      price: 1200
    },
    {
      id: 2,
      name: "window 2",
      quantity: 2,
      price: 1200
    },
    {
      id: 3,
      name: "window 3",
      quantity: 2,
      price: 1200
    }
  ];

  React.useEffect(() => {
    console.log("Hola aqui ando ejecuntandome")
  }, [])
  return (
    <React.Fragment>
      {listItemCuote.map(item =>
      (<tr key={item.id}>
        <th scope="row">{item.id}</th>
        <td>{item.name}</td>
        <td>{item.quantity}</td>
        <td>{item.price}</td>
      </tr>)
      )}
    </React.Fragment>
  )
}

ReactDOM.render(
  <ListItemQuote />,
  document.getElementById('RowsQuote')
);