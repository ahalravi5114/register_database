import { useState } from "react";
import axios from "axios";

function Login() {
  const [formData, setFormData] = useState({
    username: "",
    password: ""
  });

  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    try {
      const response = await axios.post("http://127.0.0.1:5000/login", formData);
      setMessage(response.data.message);
    } catch (error) {
      setMessage("Login failed. Invalid username or password.");
    }
  };

  return (
    <div className="flex justify-center items-center h-screen">
      <form className="bg-white p-6 rounded shadow-md w-80" onSubmit={handleSubmit}>
        <h1 className="text-xl font-bold mb-4">Login</h1>

        <div className="mb-4">
          <label className="block mb-2 text-sm font-medium">Username</label>
          <input
            type="text"
            name="username"
            value={formData.username}
            onChange={handleChange}
            className="border p-2 w-full"
            required
          />
        </div>

        <div className="mb-4">
          <label className="block mb-2 text-sm font-medium">Password</label>
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            className="border p-2 w-full"
            required
          />
        </div>

        <button type="submit" className="bg-blue-500 text-white py-2 px-4 rounded">
          Login
        </button>
        
        {message && <p className="mt-4">{message}</p>}
      </form>
    </div>
  );
}

export default Login;
