import { Title } from '../components/Title';
import { InputBox } from '../components/InputBox';
import { GuidingBox } from '../components/GuidingBox';
import { useState } from 'react';

export function PersonalPage() {
  const [projectName, setProjectName] = useState('');
  const [description, setDescription] = useState('');

  return (
    <div className='space-y-8'>
      <Title>Create New Project</Title>

      <GuidingBox>
        Please fill in the project details below. The project name is required.
      </GuidingBox>

      <div className='max-w-2xl space-y-6'>
        <InputBox
          title='Project Name'
          name='projectName'
          required
          placeholder='Enter your project name'
          value={projectName}
          onChange={setProjectName}
        />

        <InputBox
          title='Description'
          name='description'
          placeholder='Enter project description'
          value={description}
          onChange={setDescription}
        />

        <GuidingBox>
          Please fill in the repository url. The github url is required.
        </GuidingBox>
      </div>
    </div>
  );
}
