public interface IJobRespository
{
    Task<IEnumerable<JobDto>> GetJobListAsync();
}