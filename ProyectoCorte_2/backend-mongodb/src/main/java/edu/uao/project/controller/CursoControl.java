package edu.uao.project.controller;

import org.springframework.web.bind.annotation.RestController;

import edu.uao.project.model.Curso;
import edu.uao.project.service.CursoServiceIMPL;
import lombok.RequiredArgsConstructor;

import java.util.List;

import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;

@RestController
@RequestMapping("/api/v1")
@RequiredArgsConstructor
public class CursoControl {
	
	private final CursoServiceIMPL cursoService;
	
	@PostMapping("/Courses")
	public void save(@RequestBody Curso curso) {
		cursoService.save(curso);
	}
	
	@GetMapping("/Courses")
	public List<Curso> findAll(){
		return cursoService.findAll();
	}
	
	@GetMapping("/Courses/{id}")
	public Curso findById(@PathVariable String id) {
		return cursoService.findById(id).get();
	}
	@DeleteMapping("/Courses/{id}")
	public void deleteById(@PathVariable String id) {
		cursoService.deleteById(id);
	}
	@PutMapping("/Courses")
	public void update(@RequestBody Curso curso) {
		cursoService.save(curso);
		
	}
}
