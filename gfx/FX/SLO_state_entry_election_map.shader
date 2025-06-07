Includes = {
}

PixelShader =
{
	Samplers =
	{
		TextureOne =
		{
			Index = 0
			MagFilter = "Point"
			MinFilter = "Point"
			MipFilter = "None"
			AddressU = "Wrap"
			AddressV = "Wrap"
		}
		TextureTwo =
		{
			Index = 1
			MagFilter = "Point"
			MinFilter = "Point"
			MipFilter = "None"
			AddressU = "Wrap"
			AddressV = "Wrap"
		}
	}
}


VertexStruct VS_INPUT
{
    float4 vPosition  : POSITION;
    float2 vTexCoord  : TEXCOORD0;
};

VertexStruct VS_OUTPUT
{
    float4  vPosition : PDX_POSITION;
    float2  vTexCoord0 : TEXCOORD0;
};


ConstantBuffer( 0, 0 )
{
	float4x4 WorldViewProjectionMatrix; 
	float4 vFirstColor;
	float4 vSecondColor;
	float CurrentState;
};


VertexShader =
{
	MainCode VertexShader
	[[
		
		VS_OUTPUT main(const VS_INPUT v )
		{
			VS_OUTPUT Out;
		   	Out.vPosition  = mul( WorldViewProjectionMatrix, v.vPosition );
			Out.vTexCoord0  = v.vTexCoord;
			Out.vTexCoord0.y = -Out.vTexCoord0.y;
		
			return Out;
		}
		
	]]
}

PixelShader =
{
	MainCode PixelColor
	[[
		
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
			return vFirstColor;
		}
		
	]]

	MainCode PixelTexture
	[[
		
		float4 main( VS_OUTPUT v ) : PDX_COLOR
		{
			float4 OutColor = tex2D( TextureOne, v.vTexCoord0 );
			
			//No point doing operations if the alpha channel is 0
			if (OutColor.a != 0.0f){
				
				//Value between 0-100
				int CurrentStateInt = (int)(CurrentState * 100);
				
				//Get winning party and margin of victory
				int victoriousParty = CurrentStateInt / 14;
				float marginOfVictory = CurrentStateInt % 14;
				
				float3 partyRGBValue;
				
				switch(victoriousParty)
				{
					case 0:		//Communist
						partyRGBValue = float3(0.835294f, 0.0f, 0.0f);
						//RGB: 213, 0, 0
						break;
						
					case 1: 	//SocDem
						partyRGBValue = float3(0.745098f, 0.0f, 0.258824f);
						//RGB: 190, 0, 66
						break;
						
					case 2: 	//Liberal
//						partyRGBValue = float3(1.0f, 0.933334f, 0.0f);
//						//RGB: 255, 238, 0
						
						partyRGBValue = float3(0.807843f, 0.74117647f, 0.02745098f);
						//RGB: 206, 189, 7
						break;
						
					case 3: 	//Agrarian / Conservative
						partyRGBValue = float3(0.0f, 0.1490196f, 0.7294118f);
						//RGB: 0, 38, 186
						break;
						
					case 4: 	//Nationalist
						partyRGBValue = float3(0.1098039f, 0.1098039f, 0.1098039f);
						//RGB: 28, 28, 28
						break;
						
					case 5: 	//Fascist
						partyRGBValue = float3(0.54901961f, 0.22745098f, 0.0f);
						//RGB: 140, 58, 0
						break;
						
					default:	//Default / other
						partyRGBValue = float3(0.439216f, 0.439216f, 0.439216f);
						//RGB: 140, 140, 140
						break;
				}
				
				//marginOfVictory -> Between 0-13, representing the scale of victory in 2% increments.
				//0 = x<2, 1 = 2<x<4, etc.
				
				float strength = saturate(marginOfVictory / 13.0f);
				float luminance = dot(partyRGBValue, float3(0.8f, 0.8f, 0.8f));
				
				//																		Lower value = more grey, higher = more colour 
				float3 mutedColor = lerp(float3(luminance, luminance, luminance), partyRGBValue, 0.50f);
				OutColor.rgb  = lerp(mutedColor, partyRGBValue, strength);
			}
			
			return OutColor;
		}
		
	]]
}


BlendState BlendState
{
	BlendEnable = yes
	SourceBlend = "SRC_ALPHA"
	DestBlend = "INV_SRC_ALPHA"
}


Effect Color
{
	VertexShader = "VertexShader"
	PixelShader = "PixelColor"
}

Effect Texture
{
	VertexShader = "VertexShader"
	PixelShader = "PixelTexture"
}

