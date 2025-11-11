
import './App.css'

function App() {
  return (
    // Estas são as classes que o Tailwind deve compilar:
    <div className="min-h-screen bg-gray-100 p-8"> 
      <header className="text-center mb-10">
        <h1 className="text-4xl font-bold text-gray-800">
          Gerenciador de Tarefas
        </h1>
      </header>
      
      <main className="max-w-3xl mx-auto bg-white p-6 rounded-lg shadow-xl">
        {/* Este será o nosso placeholder antes de criarmos os componentes */}
        <p className="text-center text-gray-500">
          Componentes de Tarefas virão aqui.
        </p>
      </main>
    </div>
  )
}

export default App
