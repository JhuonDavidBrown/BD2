package edu.uao.project.service;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import edu.uao.project.model.Curso;
import edu.uao.project.repository.CursoRepo;
import lombok.RequiredArgsConstructor;



@Service
@RequiredArgsConstructor
public class CursoServiceIMPL {
    
    private final CursoRepo cursoRepo;
    
    public void save (Curso curso) {
    	cursoRepo.save(curso);
    }
    
    public List<Curso> findAll(){
    	return cursoRepo.findAll();
    }
    
    public Optional<Curso>findById(String id) {
    	return cursoRepo.findById(id);
    }
    
    public void deleteById(String id) {
    	cursoRepo.deleteById(id);
    }
    

}