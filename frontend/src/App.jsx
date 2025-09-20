import { useState, useEffect } from 'react'
import api from './services/api'

function App() {
  const [productos, setProductos] = useState([])
  const [form, setForm] = useState({ nombre: '', precio: '', descripcion: '' })
  const [busqueda, setBusqueda] = useState('')
  const [editId, setEditId] = useState(null) 

  // usar busqueda en el GET
  const cargarProductos = async () => {
    const res = await api.get(`/productos?nombre=${busqueda}`)
    setProductos(res.data)
  }

  const agregarProducto = async () => {
    await api.post('/productos', {
      ...form,
      precio: Number (form.precio) // convertir precio a número
    })
    setForm({ nombre: '', precio: '', descripcion: '' })
    cargarProductos()
  }

  const eliminarProducto = async (id) => {
    await api.delete(`/productos/${id}`)
    cargarProductos()
  }


  const modificarProducto = async () => {
    if (!editId) return
    await api.put(`/productos/${editId}`, {
      nombre: form.nombre,
      precio: Number(form.precio),
      descripcion: form.descripcion
    })
    setForm({ nombre: '', precio: '', descripcion: '' })
    setEditId(null)
    cargarProductos()
  }

  useEffect(() => {
    cargarProductos()
  }, [busqueda])

  //Cargar datos al formulario antes de modificar
  const editarProducto = (producto) => {
    setForm({
      nombre: producto.nombre,
      precio: producto.precio,
      descripcion: producto.descripcion
    })
    setEditId(producto.id)
  }

  return (
    <div className="p-6 max-w-xl mx-auto">
      <h1 className="text-2xl font-bold mb-4">📦 Catálogo de Productos</h1>

      <input
        type="text"
        placeholder="Buscar por nombre"
        value={busqueda}
        onChange={(e) => setBusqueda(e.target.value)}
        className="mb-4 p-2 border w-full"
      />

      <div className="mb-4">
        <input type="text" placeholder="Nombre" value={form.nombre} onChange={(e) => setForm({ ...form, nombre: e.target.value })} className="p-2 border w-full mb-2" />
        <input type="number" placeholder="Precio" value={form.precio} onChange={(e) => setForm({ ...form, precio: e.target.value })} className="p-2 border w-full mb-2" />
        <input type="text" placeholder="Descripción" value={form.descripcion} onChange={(e) => setForm({ ...form, descripcion: e.target.value })} className="p-2 border w-full mb-2" />

        {editId ? (
          <button onClick={modificarProducto} className="bg-green-500 text-white px-4 py-2 rounded">Guardar Cambios</button>
        ) : (
          <button onClick={agregarProducto} className="bg-blue-500 text-white px-4 py-2 rounded">Agregar</button>
        )}
      </div>

      <ul>
        {productos.map(p => (
          <li key={p.id} className="border p-2 mb-2 flex justify-between items-center">
            <div>
              <strong>{p.nombre}</strong> - ${p.precio}
              <p className="text-sm text-gray-600">{p.descripcion}</p>
            </div>
            <div className="space-x-2">
              <button onClick={() => editarProducto(p)} className="bg-yellow-500 text-white px-2 py-1 rounded">Editar</button>
              <button onClick={() => eliminarProducto(p.id)} className="bg-red-500 text-white px-2 py-1 rounded">Eliminar</button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  )
}

export default App
