/**
 * Configuracao do Knex, passando o parametro "client" que determina qual banco de dados será utlizado,
 * e em seguida 
 */

// import mongoose from 'mongoose'

// mongoose.Promise = global.Promise
// const connectionDB = mongoose.connect('mongodb://localhost:60000/faculdade')
//   .then(() => {
//     console.log('Mongodb conectado...');
//   }).catch(() => {
//     console.log('Erro ao conectar com o mongo');
//   })

  
  // import mongoose from 'mongoose'
  // import knex from '../database/connectDB.js';
  
  // const CursoSchema = mongoose.Schema({
  //   codigo: {
  //     type: Number,
  //     require: true
  //   },
  //   nome: {
  //     type: String,
  //     require: true
  //   }
  // })
  
  // mongoose.model('Curso', CursoSchema)
  
  // const novoCurso = mongoose.model('Curso')
  
  // new novoCurso({
  //   codigo: 3,
  //   nome: 'Engenharia Eletrônica'
  // }).save().then(() => {
  //   console.log('Curso criado com sucesso!');
  // }).catch(() => {
  //   console.log('Erro ao criar Curso!');
  // })
// export default connectionDB;