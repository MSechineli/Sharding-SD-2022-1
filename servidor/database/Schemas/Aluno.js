import mongoose from "mongoose"

const AlunoSchema = mongoose.model('Aluno', {
  ra: Number,
  nome: String,
  periodo: Number,
  cod_curso: Number
})



export default AlunoSchema