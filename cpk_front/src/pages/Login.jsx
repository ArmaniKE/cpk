import { useState } from "react";

export default function Login() {
  const [isRegister, setIsRegister] = useState(false);
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };
  
  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(isRegister ? "Регистрация" : "Вход", formData);
    // TODO: Подключить к backend API
  };

  return (
    <div className="flex items-center justify-center py-10 bg-gray-100">
      <div className="w-full max-w-md p-6 bg-white rounded-lg shadow-lg">
        <h2 className="text-xl font-semibold text-center mb-4">
          {isRegister ? "Регистрация" : "Вход"}
        </h2>
        <form onSubmit={handleSubmit} className="space-y-4">
          {isRegister && (
            <div>
              <label className="block text-sm font-medium text-gray-700">
                Имя пользователя
              </label>
              <input
                type="text"
                name="username"
                value={formData.username}
                onChange={handleChange}
                required
                className="mt-1 w-full p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500"
              />
            </div>
          )}
          <div>
            <label className="block text-sm font-medium text-gray-700">
              Электронная почта
            </label>
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
              className="mt-1 w-full p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700">
              Пароль
            </label>
            <input
              type="password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              required
              className="mt-1 w-full p-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500"
            />
          </div>
          <button
            type="submit"
            className="w-full bg-sky-500 text-white p-2 rounded-lg hover:bg-sky-600 transition"
          >
            {isRegister ? "Зарегистрироваться" : "Войти"}
          </button>
        </form>
        <p className="text-sm text-center mt-4">
          {isRegister ? "Уже есть аккаунт?" : "Нет аккаунта?"}{" "}
          <button
            type="button"
            className="text-sky-500 hover:underline"
            onClick={() => setIsRegister(!isRegister)}
          >
            {isRegister ? "Войти" : "Зарегистрироваться"}
          </button>
        </p>
      </div>
    </div>
  );
}
