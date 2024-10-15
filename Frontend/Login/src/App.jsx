import { useState } from "react";
import Register from './Register';
import Login from './Login';

function App() {
  const [isLogin, setIsLogin] = useState(true);  

  const toggleForm = () => {
    setIsLogin(!isLogin);
  };

  return (
    <div className="flex flex-col justify-center items-center h-screen">
      <div className="mb-4">
        {isLogin ? <Login /> : <Register />}
      </div>
      
      <button 
        onClick={toggleForm}
        className="bg-gray-500 text-white py-2 px-4 rounded mt-4"
      >
        {isLogin ? "Switch to Register" : "Switch to Login"}
      </button>
    </div>
  );
}

export default App;
