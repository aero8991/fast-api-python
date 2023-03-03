import React from 'react'
import "./table.css"

const Table = ({data}) => {
  return (
    <table>
      <tbody>
        <tr>
          <th>Pharmacy Name</th>
          <th>Action(Bundle)</th>
          <th>Value</th>
          <th>Routing Name</th>
          <th>Address</th>
          <th>Payee Id</th>
          <th>Payee Second ID</th>
        </tr>
        {data.data.map((item) => (
          <tr key={item.id}>
            <td>{item.Pharmacy_Report_Name}</td>
            <td>{item.Action}</td>
            <td>{item.Value}</td>
            <td>{item.RoutingName}</td>
            <td>{item.RoutingAddress1}</td>
            <td>{item.PayeeID}</td>
            <td>{item.payeeSecondID}</td>
          </tr>
        ))}
        {console.log(data)}

      </tbody>
    </table>
  );
}

export default Table
