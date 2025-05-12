import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const [orders, setOrders] = useState([]);

  useEffect(() => {
  axios.get("http://orders-service:8001/orders").then((res) => {
    setOrders(res.data);
  }).catch((error) => {
    console.error("Error al obtener órdenes:", error);
  });
}, []);


  return (
    <div>
      <h1>Órdenes</h1>
      <ul>
        {orders.map((order) => (
          <li key={order.id}>
            {order.item} - {order.quantity}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
