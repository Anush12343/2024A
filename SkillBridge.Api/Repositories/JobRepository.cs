public class JobRepository : IJobRespository
{
    public async Task<IEnumerable<JobDto>> GetJobListAsync()
    {
       return new List<JobDto>
        {
            new JobDto { Id = 1, Name = "Software Engineer",
             Description = "Develop and maintain software applications",
             MinSalary = 60000, MaxSalary = 120000},
            new JobDto { Id = 2, Name = "Product Manager",
             Description = "Manage product development and strategy",
             MinSalary = 70000, MaxSalary = 130000},
            new JobDto { Id = 3, Name = "Data Scientist",
             Description = "Analyze",
             MinSalary = 70000, MaxSalary = 130000},
        };
        
    }
}