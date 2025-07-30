import React, { useState } from 'react';
import axios from 'axios';

function InvoiceForm() {
  const [form, setForm] = useState({
    client_name: '',
    item: '',
    quantity: '',
    rate: ''
  });

  const handleChange = (e) => {
    setForm({...form, [e.target.name]: e.target.value});
  }

  const handleSubmit = async (e) => {
    e.preventDefault();
    const response = await axios.post(
      "http://127.0.0.1:8000/api/invoice/create/",
      form,
      { responseType: 'blob' }
    );
    const blob = new Blob([response.data], { type: 'application/pdf' });
    const link = document.createElement('a');
    link.href = window.URL.createObjectURL(blob);
    link.download = "invoice.pdf";
    link.click();
  }

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" name="client_name" placeholder="Client Name" onChange={handleChange} /><br/>
      <input type="text" name="item" placeholder="Item" onChange={handleChange} /><br/>
      <input type="number" name="quantity" placeholder="Quantity" onChange={handleChange} /><br/>
      <input type="number" name="rate" placeholder="Rate" onChange={handleChange} /><br/>
      <button type="submit">Generate Invoice</button>
    </form>
  );
}

export default InvoiceForm;



