package edu.uao.project.service;

import java.util.List;
import java.util.Optional;

import org.springframework.stereotype.Service;

import edu.uao.project.model.CursoNota;
import edu.uao.project.repository.CursoNotaRepo;
import lombok.RequiredArgsConstructor;


@Service
@RequiredArgsConstructor
public class CursoNotaServiceIMPL {
    
    private final CursoNotaRepo cursoNotaRepo;
    
    public void save (CursoNota cursoNota) {
    	cursoNotaRepo.save(cursoNota);
    }
    
    public List<CursoNota> findAll(){
    	return cursoNotaRepo.findAll();
    }
    
    public Optional<CursoNota>findById(String id) {
    	return cursoNotaRepo.findById(id);
    }
    
    public void deleteById(String id) {
    	cursoNotaRepo.deleteById(id);
    }
    

}