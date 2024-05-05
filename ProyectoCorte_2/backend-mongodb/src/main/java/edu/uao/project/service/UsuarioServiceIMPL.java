package edu.uao.project.service;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import edu.uao.project.model.Usuario;
import edu.uao.project.repository.UsuarioRepo;
import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class UsuarioServiceIMPL {
    
    private final UsuarioRepo usuarioRepo;
    
    public void save (Usuario usuario) {
    	usuarioRepo.save(usuario);
    }
    
    public List<Usuario> findAll(){
    	return usuarioRepo.findAll();
    }
    
    public Optional<Usuario>findById(String id) {
    	return usuarioRepo.findById(id);
    }
    
    public void deleteById(String id) {
    	usuarioRepo.deleteById(id);
    }
    

}