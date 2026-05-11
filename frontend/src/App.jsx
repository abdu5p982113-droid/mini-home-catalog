import { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const fetchCatalog = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/products');
      if (!response.ok) {
          throw new Error('Server connection failed.');
      }
      const data = await response.json();
      setProducts(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchCatalog();
  }, []);

  return (
    <div className="app-container" dir="ltr">
      <header className="header">
        <h1>Mini Home Furniture Dashboard</h1>
        <p>Digital Catalog Management</p>
      </header>

      <main>
        {loading && <p>Loading catalog...</p>}
        {error && <div className="error-msg">{error}</div>}

        <div className="products-grid">
          {products.map(product => (
            <div key={product.id} className="card">
              <h3>{product.name}</h3>
              <p><strong>Style:</strong> {product.style}</p>
              <p><strong>Material:</strong> {product.material}</p>
              <p className="price">Price: ${product.price}</p>
            </div>
          ))}
          {!loading && products.length === 0 && (
            <p>No products available currently. Add a new item via the API.</p>
          )}
        </div>
      </main>
    </div>
  );
}

export default App;