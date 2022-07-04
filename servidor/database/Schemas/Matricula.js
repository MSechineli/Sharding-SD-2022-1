import mongoose from "mongoose"

const MatriculaSchema = mongoose.model('Matricula', {
  ra: Number,
  cod_disciplina: String,
  ano: Number,
  semestre: Number,
  nota: Number,
  faltas: Number
})

export default MatriculaSchema