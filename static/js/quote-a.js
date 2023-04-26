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
    },
    ,
    {
      id: 4,
      name: "window 3",
      quantity: 2,
      price: 1200
    },
    ,
    {
      id: 5,
      name: "window 3",
      quantity: 2,
      price: 1200
    },
    ,
    {
      id: 6,
      name: "window 3",
      quantity: 2,
      price: 1200
    },
    ,
    {
      id: 7,
      name: "window 3",
      quantity: 2,
      price: 1200
    },
    ,
    {
      id: 8,
      name: "window 3",
      quantity: 2,
      price: 1200
    },
    ,
    {
      id: 9,
      name: "window 3",
      quantity: 2,
      price: 1200
    },
    ,
    {
      id: 10,
      name: "window 3",
      quantity: 2,
      price: 1200
    },
    ,
    {
      id: 11,
      name: "window 3",
      quantity: 2,
      price: 1200
    },
    ,
    {
      id: 12,
      name: "window 3",
      quantity: 2,
      price: 1200
    },
    ,
    {
      id: 13,
      name: "window 3",
      quantity: 2,
      price: 1200
    },
    ,
    {
      id: 14,
      name: "window 3",
      quantity: 2,
      price: 1200
    },

  ];

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