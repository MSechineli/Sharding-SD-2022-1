import mongoose from "mongoose"

const MatriculaSchema = mongoose.model('Matricula', {
  ra: Number,
  cod_disciplina: String,
  ano: Number,
  semestre: Number,
  nota: Number,
  faltas: Number
})

// const MatriculaSchema = mongoose.Schema({
//   ra: {
//     type: Number,
//     require: true
//   },
//   cod_disciplina: {
//     type: String,
//     require: true
//   },
//   ano: {
//     type: Number,
//     require: true
//   },
//   semestre: {
//     type: Number,
//     require: true
//   },
//   nota: {
//     type: Number,
//     require: true
//   },
//   faltas: {
//     type: Number,
//     require: true
//   }
// })

export default MatriculaSchema