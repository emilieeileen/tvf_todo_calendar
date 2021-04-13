import React, {useState} from 'react'
import axios from 'axios'

function TodoList() {
const [items, setItems] = useState([])
const [formData, updateFormData] = useState({
  name: '',
  date: ''
})

const inputFields = ['name', 'date']

function handleChange(event) {
  const { name, date, value } = event.target
  updateFormData({ ...formData, [name]: value, [date]: value})
}

function fetchTodo() {
    axios.get('/api/todos').then(
        (response) => {
            setItems(response.data)
        }
    )
 }

 async function handleSubmit(event) {
  event.preventDefault()
  
  try {
    const { data } = await axios.post('/api/todos', formData)
    console.log(data.id)
    history.push(`/todos/${data.id}`)
  } catch (err) {
    console.log(err.response)
  }
}

 return (
    <div>
      <button onClick={fetchTodo}>See Todo List</button>
      <div>
      {items.map(item => (
      <li key={item.id}>{item.name}: {item.date}</li>
      
    ))}
    </div>
    <div className="container">
      <form onSubmit={handleSubmit}>
        {inputFields.map(field => {
          return <div key={field} className="field">
            <label className="label">
              {field[0].toUpperCase() + field.slice(1)}
            </label>
            <div className="control">
              <input
                className="input"
                type="text"
                value={formData[field]}
                onChange={handleChange}
                name={field}
              />
            </div>
          </div>
        })}
        <button className="button">Submit</button>
      </form>
      
      </div>
      
     
     




        
    </div>
    );
    };
   export default TodoList