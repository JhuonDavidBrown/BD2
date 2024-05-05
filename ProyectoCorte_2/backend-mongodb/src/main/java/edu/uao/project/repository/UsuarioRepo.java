package edu.uao.project.repository;



import org.springframework.data.mongodb.repository.MongoRepository;
import org.springframework.stereotype.Repository;

import edu.uao.project.model.Usuario;

@Repository //definirla como repositorio
public interface UsuarioRepo extends MongoRepository<Usuario,String>{
	
}	