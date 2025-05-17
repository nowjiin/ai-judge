import { Title } from '../components/Title';
import { InputBox } from '../components/InputBox';
import { DescriptionInput } from '../components/DescriptionInput';
import { GuidingBox } from '../components/GuidingBox';
import { EvaluateButton } from '../components/EvaluateButton';
import { Button } from '../components/Button';
import { useState } from 'react';

export function PersonalPage() {
  const [projectName, setProjectName] = useState('');
  const [description, setDescription] = useState('');
  const [activeButtons, setActiveButtons] = useState<Set<string>>(new Set());
  const [frontendRepo, setFrontendRepo] = useState('');
  const [backendRepo, setBackendRepo] = useState('');
  const [otherRepo, setOtherRepo] = useState('');

  const handleButtonClick = (buttonName: string) => {
    setActiveButtons((prev) => {
      const newSet = new Set(prev);
      if (newSet.has(buttonName)) {
        newSet.delete(buttonName);
      } else {
        newSet.add(buttonName);
      }
      return newSet;
    });
  };

  const isFormValid = () => {
    return (
      projectName.trim() !== '' &&
      description.trim() !== '' &&
      frontendRepo.trim() !== '' &&
      backendRepo.trim() !== '' &&
      activeButtons.size > 0
    );
  };

  return (
    <main className='max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8'>
      <div className='space-y-8'>
        <Title>Snap your code!</Title>

        <GuidingBox>
          서비스의 개요를 작성할 수 있습니다.
          <br />
          설명은 구체적일수록 꼼꼼한 평가를 받을 수 있습니다.
        </GuidingBox>

        <div className='max-w-2xl space-y-6'>
          <InputBox
            title='서비스명'
            value={projectName}
            onChange={setProjectName}
            required
            placeholder='서비스명을 입력해주세요.(최대 100자)'
            maxLength={100}
          />
        </div>

        <DescriptionInput
          title='서비스 설명'
          value={description}
          onChange={setDescription}
          placeholder='서비스에 대한 간단한 설명을 입력해주세요.(최대 1000자)'
          maxLength={1000}
          required
        />

        <GuidingBox>
          평가 항목을 선택하고 1개 이상의 레포지토리 URL을 입력할 수 있습니다.
          <br />
          URL 형식이 올바른지 꼭 체크해주세요!
        </GuidingBox>

        <div className='space-y-4'>
          <div className='font-pretendard text-[20px] font-medium leading-[28px] tracking-[-0.386px] text-[#6473A0] flex items-start'>
            <span className='align-top'>평가 항목</span>
            <span className='text-red-500 text-[8px] ml-1 leading-none align-top'>
              *
            </span>
          </div>

          <div className='flex gap-4'>
            <EvaluateButton
              onClick={() => handleButtonClick('codeQuality')}
              text='Code Quality'
              isActive={activeButtons.has('codeQuality')}
            />
            <EvaluateButton
              onClick={() => handleButtonClick('projectStructure')}
              text='Project Structure'
              isActive={activeButtons.has('projectStructure')}
            />
            <EvaluateButton
              onClick={() => handleButtonClick('creativity')}
              text='Creativity'
              isActive={activeButtons.has('creativity')}
            />
          </div>
        </div>

        <div className='space-y-6'>
          <div className='font-pretendard text-[20px] font-medium leading-[28px] tracking-[-0.386px] text-[#6473A0] flex items-start'>
            <span className='align-top'>레포지토리</span>
            <span className='text-red-500 text-[8px] ml-1 leading-none align-top'>
              *
            </span>
          </div>

          <div className='space-y-4'>
            <InputBox
              title='프론트엔드 레포지토리'
              value={frontendRepo}
              onChange={setFrontendRepo}
              required
              placeholder='프론트엔드 레포지토리 URL을 입력해주세요.'
              maxLength={200}
            />

            <InputBox
              title='백엔드 레포지토리'
              value={backendRepo}
              onChange={setBackendRepo}
              required
              placeholder='백엔드 레포지토리 URL을 입력해주세요.'
              maxLength={200}
            />

            <InputBox
              title='기타 레포지토리'
              value={otherRepo}
              onChange={setOtherRepo}
              placeholder='기타 레포지토리 URL을 입력해주세요. (선택사항)'
              maxLength={200}
            />
          </div>
        </div>

        <div className='flex justify-start mt-8'>
          <Button type='submit' disabled={!isFormValid()}>
            Snap my code!
          </Button>
        </div>
      </div>
    </main>
  );
}
