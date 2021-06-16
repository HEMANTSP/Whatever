select distinct c.name from subjects c, books_subjects b where b.subject in ( select b.subject from books_subjects b , books a where a.id=b.book and a.title="Atomic Habits") and b.subject=c.id; 
